"""Main running file."""
import requests
import json
from database import *
from exceptions import WrongInputData
import logging
from logger import init_logger



logger = logging.getLogger("main")


URL = "https://spacex-production.up.railway.app"

BODY = """
{
  launches {
    mission_id
    mission_name
    rocket {
      rocket_name
      rocket_type
      rocket {
        country
        cost_per_launch
      }
    }
  }
}
"""


def get_graphql(url: str, body: str) -> dict:
    """Get graphql data.

    Args:
        url (str): url to grapg.
        body (str): body of query.

    Raises:
        WrongInputData: if input data is wrong.

    Returns:
        dict: dictionary with data from graphql.
    """
    try:
        response = requests.post(url=url, json={"query": body})
    except Exception:
        logger.info("Reqest WRONG DATA.")
        raise WrongInputData(url, body)
    else:
        logger.info("Graphql data was successfully recieved.")
        return json.loads(response.content)


if __name__ == "__main__":
  init_logger("main")
  init_database()
  graph_json = get_graphql(URL, BODY)
  for elements in graph_json["data"]["launches"]:
      set_launches(
          set_rockets(elements["rocket"]["rocket_name"],
                      elements["rocket"]["rocket_type"],
                      elements["rocket"]["rocket"]["country"],
                      elements["rocket"]["rocket"]["cost_per_launch"]
                      ),
          set_missions(elements["mission_id"][0], elements["mission_name"])
      )
  logger.info("Launches table was successfully created.")
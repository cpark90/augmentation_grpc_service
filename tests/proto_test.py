import time
import unittest

import protos.scenario_control_message_pb2 as scenario_control_message


class TestProto(unittest.TestCase):
    def __init__(self, methodName) -> None:
        super().__init__(methodName)

    def test_scenario_info(self):
        scenario_info = scenario_control_message.ScenarioInfo()
        scenario_info.id = 0
        scenario_info.data = "Success"
        self.assertEquals(scenario_info.data, "Success")

if __name__ == '__main__':
  unittest.main()
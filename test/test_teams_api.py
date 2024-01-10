# coding: utf-8

"""
    FastAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.teams_api import TeamsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_count_of_teams_counts_teams_v1_get(self):
        """Test case for count_of_teams_counts_teams_v1_get

        Count Of Teams  # noqa: E501
        """
        pass

    def test_list_teams_platforms_platform_teams_v1_get(self):
        """Test case for list_teams_platforms_platform_teams_v1_get

        List Teams  # noqa: E501
        """
        pass

    def test_list_teams_teams_v1_get(self):
        """Test case for list_teams_teams_v1_get

        List Teams  # noqa: E501
        """
        pass

    def test_team_platforms_platform_teams_v1_identifier_get(self):
        """Test case for team_platforms_platform_teams_v1_identifier_get

        Team  # noqa: E501
        """
        pass

    def test_team_teams_v1_identifier_delete(self):
        """Test case for team_teams_v1_identifier_delete

        Team  # noqa: E501
        """
        pass

    def test_team_teams_v1_identifier_get(self):
        """Test case for team_teams_v1_identifier_get

        Team  # noqa: E501
        """
        pass

    def test_team_teams_v1_identifier_put(self):
        """Test case for team_teams_v1_identifier_put

        Team  # noqa: E501
        """
        pass

    def test_team_teams_v1_post(self):
        """Test case for team_teams_v1_post

        Team  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
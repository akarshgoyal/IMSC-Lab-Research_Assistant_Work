#!/usr/bin/env python
# coding: utf-8

"""
UsersApi.py
Copyright 2015 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class UsersApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('http://localhost/MediaQ_MVC_V3/api')
            self.api_client = configuration.api_client
    
    
    def change_password(self, existing_password, password, repeat_password, **kwargs):
        """
        Changes the user's password
        Sets a new password for the user

        :param str existing_password: the user's existing password. Must be sent encrypted with sha512 (required)
        :param str password: the user's password. Must be sent encrypted with sha512 (required)
        :param str repeat_password: the repeated password. Must match password (required)
        
        :return: None
        """
        
        # verify the required parameter 'existing_password' is set
        if existing_password is None:
            raise ValueError("Missing the required parameter `existing_password` when calling `change_password`")
        
        # verify the required parameter 'password' is set
        if password is None:
            raise ValueError("Missing the required parameter `password` when calling `change_password`")
        
        # verify the required parameter 'repeat_password' is set
        if repeat_password is None:
            raise ValueError("Missing the required parameter `repeat_password` when calling `change_password`")
        
        all_params = ['existing_password', 'password', 'repeat_password']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method change_password" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/change_password'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'existing_password' in params:
            form_params['existing_password'] = params['existing_password']
        
        if 'password' in params:
            form_params['password'] = params['password']
        
        if 'repeat_password' in params:
            form_params['repeat_password'] = params['repeat_password']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def forgot_password(self, username_email, **kwargs):
        """
        Forgot password. Sends an email with a link to reset password
        This generates a random string which can be used to reset the password

        :param str username_email: the username or email (required)
        
        :return: None
        """
        
        # verify the required parameter 'username_email' is set
        if username_email is None:
            raise ValueError("Missing the required parameter `username_email` when calling `forgot_password`")
        
        all_params = ['username_email']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method forgot_password" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/forgot_password'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'username_email' in params:
            form_params['username_email'] = params['username_email']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def create_location(self, lat, lon, **kwargs):
        """
        Stores new user's location
        Stores new user's location given by latitude, longitude and optionally the accuracy in meters

        :param Number lat: latitude (required)
        :param Number lon: longitude (required)
        :param Number accuracy: accuracy 
        
        :return: None
        """
        
        # verify the required parameter 'lat' is set
        if lat is None:
            raise ValueError("Missing the required parameter `lat` when calling `create_location`")
        
        # verify the required parameter 'lon' is set
        if lon is None:
            raise ValueError("Missing the required parameter `lon` when calling `create_location`")
        
        all_params = ['lat', 'lon', 'accuracy']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method create_location" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/location'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'lat' in params:
            form_params['lat'] = params['lat']
        
        if 'lon' in params:
            form_params['lon'] = params['lon']
        
        if 'accuracy' in params:
            form_params['accuracy'] = params['accuracy']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def login_user(self, username_email, password, **kwargs):
        """
        Login user to the system
        Authenticates user

        :param str username_email: the username or email (required)
        :param str password: the user's password. Must be sent encrypted with sha512 (required)
        
        :return: None
        """
        
        # verify the required parameter 'username_email' is set
        if username_email is None:
            raise ValueError("Missing the required parameter `username_email` when calling `login_user`")
        
        # verify the required parameter 'password' is set
        if password is None:
            raise ValueError("Missing the required parameter `password` when calling `login_user`")
        
        all_params = ['username_email', 'password']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method login_user" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/login'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'username_email' in params:
            form_params['username_email'] = params['username_email']
        
        if 'password' in params:
            form_params['password'] = params['password']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def user_logout(self, **kwargs):
        """
        Log out user
        Log out user and clears session

        
        :return: None
        """
        
        all_params = []

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method user_logout" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/logout'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def create_user(self, username, email, password, repeat_password, **kwargs):
        """
        Creates a new user
        Registers a new user given the details provided. Username, email and password

        :param str username: the username (required)
        :param str email: the user's email (required)
        :param str password: the user's password. Must be sent encrypted with sha512 (required)
        :param str repeat_password: the repeated password (required)
        
        :return: None
        """
        
        # verify the required parameter 'username' is set
        if username is None:
            raise ValueError("Missing the required parameter `username` when calling `create_user`")
        
        # verify the required parameter 'email' is set
        if email is None:
            raise ValueError("Missing the required parameter `email` when calling `create_user`")
        
        # verify the required parameter 'password' is set
        if password is None:
            raise ValueError("Missing the required parameter `password` when calling `create_user`")
        
        # verify the required parameter 'repeat_password' is set
        if repeat_password is None:
            raise ValueError("Missing the required parameter `repeat_password` when calling `create_user`")
        
        all_params = ['username', 'email', 'password', 'repeat_password']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method create_user" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/register'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'username' in params:
            form_params['username'] = params['username']
        
        if 'email' in params:
            form_params['email'] = params['email']
        
        if 'password' in params:
            form_params['password'] = params['password']
        
        if 'repeat_password' in params:
            form_params['repeat_password'] = params['repeat_password']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        
    def reset_password(self, reset, password, repeat_password, **kwargs):
        """
        Resets the user's password
        Reset the forgotten password and sets a new password for the user

        :param str reset: the reset password hash string (required)
        :param str password: the user's password. Must be sent encrypted with sha512 (required)
        :param str repeat_password: the repeated password. Must match password (required)
        
        :return: None
        """
        
        # verify the required parameter 'reset' is set
        if reset is None:
            raise ValueError("Missing the required parameter `reset` when calling `reset_password`")
        
        # verify the required parameter 'password' is set
        if password is None:
            raise ValueError("Missing the required parameter `password` when calling `reset_password`")
        
        # verify the required parameter 'repeat_password' is set
        if repeat_password is None:
            raise ValueError("Missing the required parameter `repeat_password` when calling `reset_password`")
        
        all_params = ['reset', 'password', 'repeat_password']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method reset_password" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/users/reset_password/{reset}/{repeat_password}'.replace('{format}', 'json')
        method = 'PUT'

        path_params = {}
        
        if 'reset' in params:
            path_params['reset'] = params['reset']  
        
        if 'repeat_password' in params:
            path_params['repeat_password'] = params['repeat_password']  
        
        query_params = {}
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'password' in params:
            form_params['password'] = params['password']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept([])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response=None, auth_settings=auth_settings)
        









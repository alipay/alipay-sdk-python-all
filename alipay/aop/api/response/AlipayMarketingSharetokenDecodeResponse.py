#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingSharetokenDecodeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingSharetokenDecodeResponse, self).__init__()
        self._btn_one_name = None
        self._btn_one_schema = None
        self._btn_two_name = None
        self._btn_two_schema = None
        self._desc = None
        self._icon = None
        self._title = None

    @property
    def btn_one_name(self):
        return self._btn_one_name

    @btn_one_name.setter
    def btn_one_name(self, value):
        self._btn_one_name = value
    @property
    def btn_one_schema(self):
        return self._btn_one_schema

    @btn_one_schema.setter
    def btn_one_schema(self, value):
        self._btn_one_schema = value
    @property
    def btn_two_name(self):
        return self._btn_two_name

    @btn_two_name.setter
    def btn_two_name(self, value):
        self._btn_two_name = value
    @property
    def btn_two_schema(self):
        return self._btn_two_schema

    @btn_two_schema.setter
    def btn_two_schema(self, value):
        self._btn_two_schema = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingSharetokenDecodeResponse, self).parse_response_content(response_content)
        if 'btn_one_name' in response:
            self.btn_one_name = response['btn_one_name']
        if 'btn_one_schema' in response:
            self.btn_one_schema = response['btn_one_schema']
        if 'btn_two_name' in response:
            self.btn_two_name = response['btn_two_name']
        if 'btn_two_schema' in response:
            self.btn_two_schema = response['btn_two_schema']
        if 'desc' in response:
            self.desc = response['desc']
        if 'icon' in response:
            self.icon = response['icon']
        if 'title' in response:
            self.title = response['title']

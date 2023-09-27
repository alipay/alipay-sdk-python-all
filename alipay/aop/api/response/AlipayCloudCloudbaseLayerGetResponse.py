#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseLayerGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseLayerGetResponse, self).__init__()
        self._description = None
        self._display_name = None
        self._gmt_modified = None
        self._latest_layer_version_name = None
        self._layer_name = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def latest_layer_version_name(self):
        return self._latest_layer_version_name

    @latest_layer_version_name.setter
    def latest_layer_version_name(self, value):
        self._latest_layer_version_name = value
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseLayerGetResponse, self).parse_response_content(response_content)
        if 'description' in response:
            self.description = response['description']
        if 'display_name' in response:
            self.display_name = response['display_name']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'latest_layer_version_name' in response:
            self.latest_layer_version_name = response['latest_layer_version_name']
        if 'layer_name' in response:
            self.layer_name = response['layer_name']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseLayerVersionGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseLayerVersionGetResponse, self).__init__()
        self._description = None
        self._display_name = None
        self._enable_delete = None
        self._gmt_create = None
        self._image_display_names = None
        self._image_list = None
        self._layer_name = None
        self._layer_version_name = None

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
    def enable_delete(self):
        return self._enable_delete

    @enable_delete.setter
    def enable_delete(self, value):
        self._enable_delete = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def image_display_names(self):
        return self._image_display_names

    @image_display_names.setter
    def image_display_names(self, value):
        if isinstance(value, list):
            self._image_display_names = list()
            for i in value:
                self._image_display_names.append(i)
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version_name(self):
        return self._layer_version_name

    @layer_version_name.setter
    def layer_version_name(self, value):
        self._layer_version_name = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseLayerVersionGetResponse, self).parse_response_content(response_content)
        if 'description' in response:
            self.description = response['description']
        if 'display_name' in response:
            self.display_name = response['display_name']
        if 'enable_delete' in response:
            self.enable_delete = response['enable_delete']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'image_display_names' in response:
            self.image_display_names = response['image_display_names']
        if 'image_list' in response:
            self.image_list = response['image_list']
        if 'layer_name' in response:
            self.layer_name = response['layer_name']
        if 'layer_version_name' in response:
            self.layer_version_name = response['layer_version_name']

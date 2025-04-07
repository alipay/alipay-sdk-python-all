#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceAdMateriallibraryAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceAdMateriallibraryAddResponse, self).__init__()
        self._duration = None
        self._height = None
        self._material_type = None
        self._material_value = None
        self._size = None
        self._source = None
        self._status = None
        self._upload_time = None
        self._user_material_lib_id = None
        self._width = None

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        self._duration = value
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def material_value(self):
        return self._material_value

    @material_value.setter
    def material_value(self, value):
        self._material_value = value
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def upload_time(self):
        return self._upload_time

    @upload_time.setter
    def upload_time(self, value):
        self._upload_time = value
    @property
    def user_material_lib_id(self):
        return self._user_material_lib_id

    @user_material_lib_id.setter
    def user_material_lib_id(self, value):
        self._user_material_lib_id = value
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceAdMateriallibraryAddResponse, self).parse_response_content(response_content)
        if 'duration' in response:
            self.duration = response['duration']
        if 'height' in response:
            self.height = response['height']
        if 'material_type' in response:
            self.material_type = response['material_type']
        if 'material_value' in response:
            self.material_value = response['material_value']
        if 'size' in response:
            self.size = response['size']
        if 'source' in response:
            self.source = response['source']
        if 'status' in response:
            self.status = response['status']
        if 'upload_time' in response:
            self.upload_time = response['upload_time']
        if 'user_material_lib_id' in response:
            self.user_material_lib_id = response['user_material_lib_id']
        if 'width' in response:
            self.width = response['width']

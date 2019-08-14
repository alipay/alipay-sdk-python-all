#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceIotAdvertiserAdQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceIotAdvertiserAdQueryResponse, self).__init__()
        self._device_sn_list = None
        self._end_time = None
        self._ext_info = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._material_url = None
        self._plan_name = None
        self._start_time = None
        self._status = None

    @property
    def device_sn_list(self):
        return self._device_sn_list

    @device_sn_list.setter
    def device_sn_list(self, value):
        if isinstance(value, list):
            self._device_sn_list = list()
            for i in value:
                self._device_sn_list.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceIotAdvertiserAdQueryResponse, self).parse_response_content(response_content)
        if 'device_sn_list' in response:
            self.device_sn_list = response['device_sn_list']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'id' in response:
            self.id = response['id']
        if 'material_url' in response:
            self.material_url = response['material_url']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']

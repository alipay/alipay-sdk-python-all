#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubVenueAuditStatus import SubVenueAuditStatus


class AlipayCommerceSportsVenueSimpleCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsVenueSimpleCreateResponse, self).__init__()
        self._desc = None
        self._out_venue_id = None
        self._sub_venue_list = None
        self._venue_id = None
        self._venue_status = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def out_venue_id(self):
        return self._out_venue_id

    @out_venue_id.setter
    def out_venue_id(self, value):
        self._out_venue_id = value
    @property
    def sub_venue_list(self):
        return self._sub_venue_list

    @sub_venue_list.setter
    def sub_venue_list(self, value):
        if isinstance(value, list):
            self._sub_venue_list = list()
            for i in value:
                if isinstance(i, SubVenueAuditStatus):
                    self._sub_venue_list.append(i)
                else:
                    self._sub_venue_list.append(SubVenueAuditStatus.from_alipay_dict(i))
    @property
    def venue_id(self):
        return self._venue_id

    @venue_id.setter
    def venue_id(self, value):
        self._venue_id = value
    @property
    def venue_status(self):
        return self._venue_status

    @venue_status.setter
    def venue_status(self, value):
        self._venue_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsVenueSimpleCreateResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'out_venue_id' in response:
            self.out_venue_id = response['out_venue_id']
        if 'sub_venue_list' in response:
            self.sub_venue_list = response['sub_venue_list']
        if 'venue_id' in response:
            self.venue_id = response['venue_id']
        if 'venue_status' in response:
            self.venue_status = response['venue_status']

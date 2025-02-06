#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudpromoTravelPicCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelPicCreateResponse, self).__init__()
        self._template_id = None
        self._travel_pic = None

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def travel_pic(self):
        return self._travel_pic

    @travel_pic.setter
    def travel_pic(self, value):
        self._travel_pic = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelPicCreateResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'travel_pic' in response:
            self.travel_pic = response['travel_pic']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotvspUserwithimageCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotvspUserwithimageCreateResponse, self).__init__()
        self._similar_vid = None
        self._similar_vid_list = None
        self._vid = None

    @property
    def similar_vid(self):
        return self._similar_vid

    @similar_vid.setter
    def similar_vid(self, value):
        self._similar_vid = value
    @property
    def similar_vid_list(self):
        return self._similar_vid_list

    @similar_vid_list.setter
    def similar_vid_list(self, value):
        if isinstance(value, list):
            self._similar_vid_list = list()
            for i in value:
                self._similar_vid_list.append(i)
    @property
    def vid(self):
        return self._vid

    @vid.setter
    def vid(self, value):
        self._vid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotvspUserwithimageCreateResponse, self).parse_response_content(response_content)
        if 'similar_vid' in response:
            self.similar_vid = response['similar_vid']
        if 'similar_vid_list' in response:
            self.similar_vid_list = response['similar_vid_list']
        if 'vid' in response:
            self.vid = response['vid']

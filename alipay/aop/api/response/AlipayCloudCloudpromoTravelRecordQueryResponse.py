#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiRecord import PoiRecord


class AlipayCloudCloudpromoTravelRecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoTravelRecordQueryResponse, self).__init__()
        self._logo = None
        self._poi_list = None
        self._share_desc = None
        self._title = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def poi_list(self):
        return self._poi_list

    @poi_list.setter
    def poi_list(self, value):
        if isinstance(value, list):
            self._poi_list = list()
            for i in value:
                if isinstance(i, PoiRecord):
                    self._poi_list.append(i)
                else:
                    self._poi_list.append(PoiRecord.from_alipay_dict(i))
    @property
    def share_desc(self):
        return self._share_desc

    @share_desc.setter
    def share_desc(self, value):
        self._share_desc = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoTravelRecordQueryResponse, self).parse_response_content(response_content)
        if 'logo' in response:
            self.logo = response['logo']
        if 'poi_list' in response:
            self.poi_list = response['poi_list']
        if 'share_desc' in response:
            self.share_desc = response['share_desc']
        if 'title' in response:
            self.title = response['title']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PoiTagInfo import PoiTagInfo


class AlipayCloudCloudpromoCustomroutePoiQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoCustomroutePoiQueryResponse, self).__init__()
        self._poi_tag_info_list = None
        self._selected_item_id_list = None

    @property
    def poi_tag_info_list(self):
        return self._poi_tag_info_list

    @poi_tag_info_list.setter
    def poi_tag_info_list(self, value):
        if isinstance(value, list):
            self._poi_tag_info_list = list()
            for i in value:
                if isinstance(i, PoiTagInfo):
                    self._poi_tag_info_list.append(i)
                else:
                    self._poi_tag_info_list.append(PoiTagInfo.from_alipay_dict(i))
    @property
    def selected_item_id_list(self):
        return self._selected_item_id_list

    @selected_item_id_list.setter
    def selected_item_id_list(self, value):
        if isinstance(value, list):
            self._selected_item_id_list = list()
            for i in value:
                self._selected_item_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoCustomroutePoiQueryResponse, self).parse_response_content(response_content)
        if 'poi_tag_info_list' in response:
            self.poi_tag_info_list = response['poi_tag_info_list']
        if 'selected_item_id_list' in response:
            self.selected_item_id_list = response['selected_item_id_list']

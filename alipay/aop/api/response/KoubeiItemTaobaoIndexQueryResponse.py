#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbItemInfo import KbItemInfo


class KoubeiItemTaobaoIndexQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemTaobaoIndexQueryResponse, self).__init__()
        self._column_title = None
        self._ext_info = None
        self._item_list = None
        self._time_icon = None
        self._time_title = None
        self._url = None

    @property
    def column_title(self):
        return self._column_title

    @column_title.setter
    def column_title(self, value):
        self._column_title = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, KbItemInfo):
                    self._item_list.append(i)
                else:
                    self._item_list.append(KbItemInfo.from_alipay_dict(i))
    @property
    def time_icon(self):
        return self._time_icon

    @time_icon.setter
    def time_icon(self, value):
        self._time_icon = value
    @property
    def time_title(self):
        return self._time_title

    @time_title.setter
    def time_title(self, value):
        self._time_title = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(KoubeiItemTaobaoIndexQueryResponse, self).parse_response_content(response_content)
        if 'column_title' in response:
            self.column_title = response['column_title']
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'time_icon' in response:
            self.time_icon = response['time_icon']
        if 'time_title' in response:
            self.time_title = response['time_title']
        if 'url' in response:
            self.url = response['url']

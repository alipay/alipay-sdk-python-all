#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OpenItem import OpenItem
from alipay.aop.api.domain.OpenItem import OpenItem
from alipay.aop.api.domain.OpenItem import OpenItem


class KoubeiQualityTestCloudacptItemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiQualityTestCloudacptItemQueryResponse, self).__init__()
        self._activity_id = None
        self._batch_id = None
        self._batch_status = None
        self._fail_list = None
        self._fail_num = None
        self._item_list = None
        self._item_num = None
        self._pass_list = None
        self._pass_num = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value
    @property
    def fail_list(self):
        return self._fail_list

    @fail_list.setter
    def fail_list(self, value):
        if isinstance(value, list):
            self._fail_list = list()
            for i in value:
                if isinstance(i, OpenItem):
                    self._fail_list.append(i)
                else:
                    self._fail_list.append(OpenItem.from_alipay_dict(i))
    @property
    def fail_num(self):
        return self._fail_num

    @fail_num.setter
    def fail_num(self, value):
        self._fail_num = value
    @property
    def item_list(self):
        return self._item_list

    @item_list.setter
    def item_list(self, value):
        if isinstance(value, list):
            self._item_list = list()
            for i in value:
                if isinstance(i, OpenItem):
                    self._item_list.append(i)
                else:
                    self._item_list.append(OpenItem.from_alipay_dict(i))
    @property
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, value):
        self._item_num = value
    @property
    def pass_list(self):
        return self._pass_list

    @pass_list.setter
    def pass_list(self, value):
        if isinstance(value, list):
            self._pass_list = list()
            for i in value:
                if isinstance(i, OpenItem):
                    self._pass_list.append(i)
                else:
                    self._pass_list.append(OpenItem.from_alipay_dict(i))
    @property
    def pass_num(self):
        return self._pass_num

    @pass_num.setter
    def pass_num(self, value):
        self._pass_num = value

    def parse_response_content(self, response_content):
        response = super(KoubeiQualityTestCloudacptItemQueryResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'batch_id' in response:
            self.batch_id = response['batch_id']
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
        if 'fail_list' in response:
            self.fail_list = response['fail_list']
        if 'fail_num' in response:
            self.fail_num = response['fail_num']
        if 'item_list' in response:
            self.item_list = response['item_list']
        if 'item_num' in response:
            self.item_num = response['item_num']
        if 'pass_list' in response:
            self.pass_list = response['pass_list']
        if 'pass_num' in response:
            self.pass_num = response['pass_num']

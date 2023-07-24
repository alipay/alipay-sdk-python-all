#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MallFile import MallFile
from alipay.aop.api.domain.PunchoutOrderItem import PunchoutOrderItem


class MallReceivePrRequest(object):

    def __init__(self):
        self._app_code = None
        self._fix_user_id = None
        self._mall_files = None
        self._order_items = None
        self._out_pur_req_id = None
        self._pur_req_id = None

    @property
    def app_code(self):
        return self._app_code

    @app_code.setter
    def app_code(self, value):
        self._app_code = value
    @property
    def fix_user_id(self):
        return self._fix_user_id

    @fix_user_id.setter
    def fix_user_id(self, value):
        self._fix_user_id = value
    @property
    def mall_files(self):
        return self._mall_files

    @mall_files.setter
    def mall_files(self, value):
        if isinstance(value, list):
            self._mall_files = list()
            for i in value:
                if isinstance(i, MallFile):
                    self._mall_files.append(i)
                else:
                    self._mall_files.append(MallFile.from_alipay_dict(i))
    @property
    def order_items(self):
        return self._order_items

    @order_items.setter
    def order_items(self, value):
        if isinstance(value, list):
            self._order_items = list()
            for i in value:
                if isinstance(i, PunchoutOrderItem):
                    self._order_items.append(i)
                else:
                    self._order_items.append(PunchoutOrderItem.from_alipay_dict(i))
    @property
    def out_pur_req_id(self):
        return self._out_pur_req_id

    @out_pur_req_id.setter
    def out_pur_req_id(self, value):
        self._out_pur_req_id = value
    @property
    def pur_req_id(self):
        return self._pur_req_id

    @pur_req_id.setter
    def pur_req_id(self, value):
        self._pur_req_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_code:
            if hasattr(self.app_code, 'to_alipay_dict'):
                params['app_code'] = self.app_code.to_alipay_dict()
            else:
                params['app_code'] = self.app_code
        if self.fix_user_id:
            if hasattr(self.fix_user_id, 'to_alipay_dict'):
                params['fix_user_id'] = self.fix_user_id.to_alipay_dict()
            else:
                params['fix_user_id'] = self.fix_user_id
        if self.mall_files:
            if isinstance(self.mall_files, list):
                for i in range(0, len(self.mall_files)):
                    element = self.mall_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mall_files[i] = element.to_alipay_dict()
            if hasattr(self.mall_files, 'to_alipay_dict'):
                params['mall_files'] = self.mall_files.to_alipay_dict()
            else:
                params['mall_files'] = self.mall_files
        if self.order_items:
            if isinstance(self.order_items, list):
                for i in range(0, len(self.order_items)):
                    element = self.order_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_items[i] = element.to_alipay_dict()
            if hasattr(self.order_items, 'to_alipay_dict'):
                params['order_items'] = self.order_items.to_alipay_dict()
            else:
                params['order_items'] = self.order_items
        if self.out_pur_req_id:
            if hasattr(self.out_pur_req_id, 'to_alipay_dict'):
                params['out_pur_req_id'] = self.out_pur_req_id.to_alipay_dict()
            else:
                params['out_pur_req_id'] = self.out_pur_req_id
        if self.pur_req_id:
            if hasattr(self.pur_req_id, 'to_alipay_dict'):
                params['pur_req_id'] = self.pur_req_id.to_alipay_dict()
            else:
                params['pur_req_id'] = self.pur_req_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MallReceivePrRequest()
        if 'app_code' in d:
            o.app_code = d['app_code']
        if 'fix_user_id' in d:
            o.fix_user_id = d['fix_user_id']
        if 'mall_files' in d:
            o.mall_files = d['mall_files']
        if 'order_items' in d:
            o.order_items = d['order_items']
        if 'out_pur_req_id' in d:
            o.out_pur_req_id = d['out_pur_req_id']
        if 'pur_req_id' in d:
            o.pur_req_id = d['pur_req_id']
        return o



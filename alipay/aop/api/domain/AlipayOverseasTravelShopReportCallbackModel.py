#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShopReportProgressInfo import ShopReportProgressInfo


class AlipayOverseasTravelShopReportCallbackModel(object):

    def __init__(self):
        self._data_version = None
        self._out_shop_id = None
        self._progress_info = None
        self._result_code = None
        self._result_message = None
        self._result_status = None

    @property
    def data_version(self):
        return self._data_version

    @data_version.setter
    def data_version(self, value):
        self._data_version = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def progress_info(self):
        return self._progress_info

    @progress_info.setter
    def progress_info(self, value):
        if isinstance(value, ShopReportProgressInfo):
            self._progress_info = value
        else:
            self._progress_info = ShopReportProgressInfo.from_alipay_dict(value)
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.data_version:
            if hasattr(self.data_version, 'to_alipay_dict'):
                params['data_version'] = self.data_version.to_alipay_dict()
            else:
                params['data_version'] = self.data_version
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.progress_info:
            if hasattr(self.progress_info, 'to_alipay_dict'):
                params['progress_info'] = self.progress_info.to_alipay_dict()
            else:
                params['progress_info'] = self.progress_info
        if self.result_code:
            if hasattr(self.result_code, 'to_alipay_dict'):
                params['result_code'] = self.result_code.to_alipay_dict()
            else:
                params['result_code'] = self.result_code
        if self.result_message:
            if hasattr(self.result_message, 'to_alipay_dict'):
                params['result_message'] = self.result_message.to_alipay_dict()
            else:
                params['result_message'] = self.result_message
        if self.result_status:
            if hasattr(self.result_status, 'to_alipay_dict'):
                params['result_status'] = self.result_status.to_alipay_dict()
            else:
                params['result_status'] = self.result_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelShopReportCallbackModel()
        if 'data_version' in d:
            o.data_version = d['data_version']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'progress_info' in d:
            o.progress_info = d['progress_info']
        if 'result_code' in d:
            o.result_code = d['result_code']
        if 'result_message' in d:
            o.result_message = d['result_message']
        if 'result_status' in d:
            o.result_status = d['result_status']
        return o



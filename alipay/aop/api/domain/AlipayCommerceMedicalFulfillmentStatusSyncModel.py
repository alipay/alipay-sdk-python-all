#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FulfillmentDataInfo import FulfillmentDataInfo


class AlipayCommerceMedicalFulfillmentStatusSyncModel(object):

    def __init__(self):
        self._fulfillment_data = None
        self._fulfillment_id = None
        self._fulfillment_status = None
        self._fulfillment_status_desc = None
        self._open_id = None
        self._out_biz_no = None
        self._trade_order_id = None
        self._type = None
        self._user_id = None

    @property
    def fulfillment_data(self):
        return self._fulfillment_data

    @fulfillment_data.setter
    def fulfillment_data(self, value):
        if isinstance(value, FulfillmentDataInfo):
            self._fulfillment_data = value
        else:
            self._fulfillment_data = FulfillmentDataInfo.from_alipay_dict(value)
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def fulfillment_status(self):
        return self._fulfillment_status

    @fulfillment_status.setter
    def fulfillment_status(self, value):
        self._fulfillment_status = value
    @property
    def fulfillment_status_desc(self):
        return self._fulfillment_status_desc

    @fulfillment_status_desc.setter
    def fulfillment_status_desc(self, value):
        self._fulfillment_status_desc = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fulfillment_data:
            if hasattr(self.fulfillment_data, 'to_alipay_dict'):
                params['fulfillment_data'] = self.fulfillment_data.to_alipay_dict()
            else:
                params['fulfillment_data'] = self.fulfillment_data
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.fulfillment_status:
            if hasattr(self.fulfillment_status, 'to_alipay_dict'):
                params['fulfillment_status'] = self.fulfillment_status.to_alipay_dict()
            else:
                params['fulfillment_status'] = self.fulfillment_status
        if self.fulfillment_status_desc:
            if hasattr(self.fulfillment_status_desc, 'to_alipay_dict'):
                params['fulfillment_status_desc'] = self.fulfillment_status_desc.to_alipay_dict()
            else:
                params['fulfillment_status_desc'] = self.fulfillment_status_desc
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalFulfillmentStatusSyncModel()
        if 'fulfillment_data' in d:
            o.fulfillment_data = d['fulfillment_data']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'fulfillment_status' in d:
            o.fulfillment_status = d['fulfillment_status']
        if 'fulfillment_status_desc' in d:
            o.fulfillment_status_desc = d['fulfillment_status_desc']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o



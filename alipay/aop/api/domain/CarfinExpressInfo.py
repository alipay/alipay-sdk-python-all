#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.XhExpressPostInfo import XhExpressPostInfo


class CarfinExpressInfo(object):

    def __init__(self):
        self._courier_name = None
        self._courier_phone = None
        self._express_org_name = None
        self._sender_info = None
        self._tracking_no = None

    @property
    def courier_name(self):
        return self._courier_name

    @courier_name.setter
    def courier_name(self, value):
        self._courier_name = value
    @property
    def courier_phone(self):
        return self._courier_phone

    @courier_phone.setter
    def courier_phone(self, value):
        self._courier_phone = value
    @property
    def express_org_name(self):
        return self._express_org_name

    @express_org_name.setter
    def express_org_name(self, value):
        self._express_org_name = value
    @property
    def sender_info(self):
        return self._sender_info

    @sender_info.setter
    def sender_info(self, value):
        if isinstance(value, XhExpressPostInfo):
            self._sender_info = value
        else:
            self._sender_info = XhExpressPostInfo.from_alipay_dict(value)
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.courier_name:
            if hasattr(self.courier_name, 'to_alipay_dict'):
                params['courier_name'] = self.courier_name.to_alipay_dict()
            else:
                params['courier_name'] = self.courier_name
        if self.courier_phone:
            if hasattr(self.courier_phone, 'to_alipay_dict'):
                params['courier_phone'] = self.courier_phone.to_alipay_dict()
            else:
                params['courier_phone'] = self.courier_phone
        if self.express_org_name:
            if hasattr(self.express_org_name, 'to_alipay_dict'):
                params['express_org_name'] = self.express_org_name.to_alipay_dict()
            else:
                params['express_org_name'] = self.express_org_name
        if self.sender_info:
            if hasattr(self.sender_info, 'to_alipay_dict'):
                params['sender_info'] = self.sender_info.to_alipay_dict()
            else:
                params['sender_info'] = self.sender_info
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinExpressInfo()
        if 'courier_name' in d:
            o.courier_name = d['courier_name']
        if 'courier_phone' in d:
            o.courier_phone = d['courier_phone']
        if 'express_org_name' in d:
            o.express_org_name = d['express_org_name']
        if 'sender_info' in d:
            o.sender_info = d['sender_info']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        return o



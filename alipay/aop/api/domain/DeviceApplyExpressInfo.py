#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeviceApplyExpressDetail import DeviceApplyExpressDetail


class DeviceApplyExpressInfo(object):

    def __init__(self):
        self._express_detail_list = None
        self._mail_no = None

    @property
    def express_detail_list(self):
        return self._express_detail_list

    @express_detail_list.setter
    def express_detail_list(self, value):
        if isinstance(value, list):
            self._express_detail_list = list()
            for i in value:
                if isinstance(i, DeviceApplyExpressDetail):
                    self._express_detail_list.append(i)
                else:
                    self._express_detail_list.append(DeviceApplyExpressDetail.from_alipay_dict(i))
    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, value):
        self._mail_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.express_detail_list:
            if isinstance(self.express_detail_list, list):
                for i in range(0, len(self.express_detail_list)):
                    element = self.express_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.express_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.express_detail_list, 'to_alipay_dict'):
                params['express_detail_list'] = self.express_detail_list.to_alipay_dict()
            else:
                params['express_detail_list'] = self.express_detail_list
        if self.mail_no:
            if hasattr(self.mail_no, 'to_alipay_dict'):
                params['mail_no'] = self.mail_no.to_alipay_dict()
            else:
                params['mail_no'] = self.mail_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceApplyExpressInfo()
        if 'express_detail_list' in d:
            o.express_detail_list = d['express_detail_list']
        if 'mail_no' in d:
            o.mail_no = d['mail_no']
        return o



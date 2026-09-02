#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentEcSignerDTO import RentEcSignerDTO


class AlipayCommerceRentOrderEcsignApplyModel(object):

    def __init__(self):
        self._additional_info = None
        self._biz_no = None
        self._ec_template_codes = None
        self._ecsign_notify_url = None
        self._order_id = None
        self._signers = None

    @property
    def additional_info(self):
        return self._additional_info

    @additional_info.setter
    def additional_info(self, value):
        self._additional_info = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ec_template_codes(self):
        return self._ec_template_codes

    @ec_template_codes.setter
    def ec_template_codes(self, value):
        if isinstance(value, list):
            self._ec_template_codes = list()
            for i in value:
                self._ec_template_codes.append(i)
    @property
    def ecsign_notify_url(self):
        return self._ecsign_notify_url

    @ecsign_notify_url.setter
    def ecsign_notify_url(self, value):
        self._ecsign_notify_url = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def signers(self):
        return self._signers

    @signers.setter
    def signers(self, value):
        if isinstance(value, list):
            self._signers = list()
            for i in value:
                if isinstance(i, RentEcSignerDTO):
                    self._signers.append(i)
                else:
                    self._signers.append(RentEcSignerDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.additional_info:
            if hasattr(self.additional_info, 'to_alipay_dict'):
                params['additional_info'] = self.additional_info.to_alipay_dict()
            else:
                params['additional_info'] = self.additional_info
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ec_template_codes:
            if isinstance(self.ec_template_codes, list):
                for i in range(0, len(self.ec_template_codes)):
                    element = self.ec_template_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ec_template_codes[i] = element.to_alipay_dict()
            if hasattr(self.ec_template_codes, 'to_alipay_dict'):
                params['ec_template_codes'] = self.ec_template_codes.to_alipay_dict()
            else:
                params['ec_template_codes'] = self.ec_template_codes
        if self.ecsign_notify_url:
            if hasattr(self.ecsign_notify_url, 'to_alipay_dict'):
                params['ecsign_notify_url'] = self.ecsign_notify_url.to_alipay_dict()
            else:
                params['ecsign_notify_url'] = self.ecsign_notify_url
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.signers:
            if isinstance(self.signers, list):
                for i in range(0, len(self.signers)):
                    element = self.signers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.signers[i] = element.to_alipay_dict()
            if hasattr(self.signers, 'to_alipay_dict'):
                params['signers'] = self.signers.to_alipay_dict()
            else:
                params['signers'] = self.signers
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentOrderEcsignApplyModel()
        if 'additional_info' in d:
            o.additional_info = d['additional_info']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ec_template_codes' in d:
            o.ec_template_codes = d['ec_template_codes']
        if 'ecsign_notify_url' in d:
            o.ecsign_notify_url = d['ecsign_notify_url']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'signers' in d:
            o.signers = d['signers']
        return o



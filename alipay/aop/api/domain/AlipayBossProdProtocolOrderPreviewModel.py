#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ContactInfomation import ContactInfomation
from alipay.aop.api.domain.MerchantInformation import MerchantInformation
from alipay.aop.api.domain.SalePlanInfo import SalePlanInfo


class AlipayBossProdProtocolOrderPreviewModel(object):

    def __init__(self):
        self._card_nos = None
        self._contact_info = None
        self._include_custom_protocol = None
        self._merchant_info = None
        self._need_file = None
        self._need_fill_item = None
        self._need_html = None
        self._sale_plans = None
        self._source = None

    @property
    def card_nos(self):
        return self._card_nos

    @card_nos.setter
    def card_nos(self, value):
        if isinstance(value, list):
            self._card_nos = list()
            for i in value:
                self._card_nos.append(i)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ContactInfomation):
            self._contact_info = value
        else:
            self._contact_info = ContactInfomation.from_alipay_dict(value)
    @property
    def include_custom_protocol(self):
        return self._include_custom_protocol

    @include_custom_protocol.setter
    def include_custom_protocol(self, value):
        self._include_custom_protocol = value
    @property
    def merchant_info(self):
        return self._merchant_info

    @merchant_info.setter
    def merchant_info(self, value):
        if isinstance(value, MerchantInformation):
            self._merchant_info = value
        else:
            self._merchant_info = MerchantInformation.from_alipay_dict(value)
    @property
    def need_file(self):
        return self._need_file

    @need_file.setter
    def need_file(self, value):
        self._need_file = value
    @property
    def need_fill_item(self):
        return self._need_fill_item

    @need_fill_item.setter
    def need_fill_item(self, value):
        self._need_fill_item = value
    @property
    def need_html(self):
        return self._need_html

    @need_html.setter
    def need_html(self, value):
        self._need_html = value
    @property
    def sale_plans(self):
        return self._sale_plans

    @sale_plans.setter
    def sale_plans(self, value):
        if isinstance(value, SalePlanInfo):
            self._sale_plans = value
        else:
            self._sale_plans = SalePlanInfo.from_alipay_dict(value)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_nos:
            if isinstance(self.card_nos, list):
                for i in range(0, len(self.card_nos)):
                    element = self.card_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.card_nos[i] = element.to_alipay_dict()
            if hasattr(self.card_nos, 'to_alipay_dict'):
                params['card_nos'] = self.card_nos.to_alipay_dict()
            else:
                params['card_nos'] = self.card_nos
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.include_custom_protocol:
            if hasattr(self.include_custom_protocol, 'to_alipay_dict'):
                params['include_custom_protocol'] = self.include_custom_protocol.to_alipay_dict()
            else:
                params['include_custom_protocol'] = self.include_custom_protocol
        if self.merchant_info:
            if hasattr(self.merchant_info, 'to_alipay_dict'):
                params['merchant_info'] = self.merchant_info.to_alipay_dict()
            else:
                params['merchant_info'] = self.merchant_info
        if self.need_file:
            if hasattr(self.need_file, 'to_alipay_dict'):
                params['need_file'] = self.need_file.to_alipay_dict()
            else:
                params['need_file'] = self.need_file
        if self.need_fill_item:
            if hasattr(self.need_fill_item, 'to_alipay_dict'):
                params['need_fill_item'] = self.need_fill_item.to_alipay_dict()
            else:
                params['need_fill_item'] = self.need_fill_item
        if self.need_html:
            if hasattr(self.need_html, 'to_alipay_dict'):
                params['need_html'] = self.need_html.to_alipay_dict()
            else:
                params['need_html'] = self.need_html
        if self.sale_plans:
            if hasattr(self.sale_plans, 'to_alipay_dict'):
                params['sale_plans'] = self.sale_plans.to_alipay_dict()
            else:
                params['sale_plans'] = self.sale_plans
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossProdProtocolOrderPreviewModel()
        if 'card_nos' in d:
            o.card_nos = d['card_nos']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'include_custom_protocol' in d:
            o.include_custom_protocol = d['include_custom_protocol']
        if 'merchant_info' in d:
            o.merchant_info = d['merchant_info']
        if 'need_file' in d:
            o.need_file = d['need_file']
        if 'need_fill_item' in d:
            o.need_fill_item = d['need_fill_item']
        if 'need_html' in d:
            o.need_html = d['need_html']
        if 'sale_plans' in d:
            o.sale_plans = d['sale_plans']
        if 'source' in d:
            o.source = d['source']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PhoneCardAddressModel import PhoneCardAddressModel


class AlipayCommerceAcommunicationDistributionPhonecardagreementQueryModel(object):

    def __init__(self):
        self._cert_name = None
        self._cert_no = None
        self._contact_phone_number = None
        self._item_id = None
        self._phone_card_address = None
        self._phone_num = None

    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def contact_phone_number(self):
        return self._contact_phone_number

    @contact_phone_number.setter
    def contact_phone_number(self, value):
        self._contact_phone_number = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def phone_card_address(self):
        return self._phone_card_address

    @phone_card_address.setter
    def phone_card_address(self, value):
        if isinstance(value, PhoneCardAddressModel):
            self._phone_card_address = value
        else:
            self._phone_card_address = PhoneCardAddressModel.from_alipay_dict(value)
    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, value):
        self._phone_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.contact_phone_number:
            if hasattr(self.contact_phone_number, 'to_alipay_dict'):
                params['contact_phone_number'] = self.contact_phone_number.to_alipay_dict()
            else:
                params['contact_phone_number'] = self.contact_phone_number
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.phone_card_address:
            if hasattr(self.phone_card_address, 'to_alipay_dict'):
                params['phone_card_address'] = self.phone_card_address.to_alipay_dict()
            else:
                params['phone_card_address'] = self.phone_card_address
        if self.phone_num:
            if hasattr(self.phone_num, 'to_alipay_dict'):
                params['phone_num'] = self.phone_num.to_alipay_dict()
            else:
                params['phone_num'] = self.phone_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionPhonecardagreementQueryModel()
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'phone_card_address' in d:
            o.phone_card_address = d['phone_card_address']
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        return o



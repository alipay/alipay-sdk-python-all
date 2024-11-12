#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PhoneCardAddressModel import PhoneCardAddressModel
from alipay.aop.api.domain.PhoneCardShippingAddressModel import PhoneCardShippingAddressModel


class AlipayCommerceAcommunicationDistributionPhonecardorderCreateModel(object):

    def __init__(self):
        self._agreement_request_id = None
        self._cert_name = None
        self._cert_no = None
        self._channel = None
        self._check_code = None
        self._contact_phone_number = None
        self._item_id = None
        self._order_id = None
        self._order_total_fee = None
        self._page_id = None
        self._phone_card_address = None
        self._phone_num = None
        self._shipping_address = None

    @property
    def agreement_request_id(self):
        return self._agreement_request_id

    @agreement_request_id.setter
    def agreement_request_id(self, value):
        self._agreement_request_id = value
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
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def check_code(self):
        return self._check_code

    @check_code.setter
    def check_code(self, value):
        self._check_code = value
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
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_total_fee(self):
        return self._order_total_fee

    @order_total_fee.setter
    def order_total_fee(self, value):
        self._order_total_fee = value
    @property
    def page_id(self):
        return self._page_id

    @page_id.setter
    def page_id(self, value):
        self._page_id = value
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
    @property
    def shipping_address(self):
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, value):
        if isinstance(value, PhoneCardShippingAddressModel):
            self._shipping_address = value
        else:
            self._shipping_address = PhoneCardShippingAddressModel.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_request_id:
            if hasattr(self.agreement_request_id, 'to_alipay_dict'):
                params['agreement_request_id'] = self.agreement_request_id.to_alipay_dict()
            else:
                params['agreement_request_id'] = self.agreement_request_id
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
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.check_code:
            if hasattr(self.check_code, 'to_alipay_dict'):
                params['check_code'] = self.check_code.to_alipay_dict()
            else:
                params['check_code'] = self.check_code
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
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_total_fee:
            if hasattr(self.order_total_fee, 'to_alipay_dict'):
                params['order_total_fee'] = self.order_total_fee.to_alipay_dict()
            else:
                params['order_total_fee'] = self.order_total_fee
        if self.page_id:
            if hasattr(self.page_id, 'to_alipay_dict'):
                params['page_id'] = self.page_id.to_alipay_dict()
            else:
                params['page_id'] = self.page_id
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
        if self.shipping_address:
            if hasattr(self.shipping_address, 'to_alipay_dict'):
                params['shipping_address'] = self.shipping_address.to_alipay_dict()
            else:
                params['shipping_address'] = self.shipping_address
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationDistributionPhonecardorderCreateModel()
        if 'agreement_request_id' in d:
            o.agreement_request_id = d['agreement_request_id']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'channel' in d:
            o.channel = d['channel']
        if 'check_code' in d:
            o.check_code = d['check_code']
        if 'contact_phone_number' in d:
            o.contact_phone_number = d['contact_phone_number']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_total_fee' in d:
            o.order_total_fee = d['order_total_fee']
        if 'page_id' in d:
            o.page_id = d['page_id']
        if 'phone_card_address' in d:
            o.phone_card_address = d['phone_card_address']
        if 'phone_num' in d:
            o.phone_num = d['phone_num']
        if 'shipping_address' in d:
            o.shipping_address = d['shipping_address']
        return o



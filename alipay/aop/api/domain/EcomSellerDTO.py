#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsOpenApplicationInfoDTO import InsOpenApplicationInfoDTO


class EcomSellerDTO(object):

    def __init__(self):
        self._address = None
        self._alipay_id = None
        self._alipay_open_id = None
        self._application_info = None
        self._attributes = None
        self._bank_card_holder_name = None
        self._bank_card_no = None
        self._bank_id = None
        self._bank_name = None
        self._bill_account_type = None
        self._id_card_no = None
        self._id_card_type = None
        self._main_cat_order_count_of_platform = None
        self._main_cat_refund_exchange_rate_of_platform = None
        self._phone = None
        self._real_name = None
        self._seller_id = None
        self._seller_nick = None
        self._seller_order_count = None
        self._seller_order_refund_exchange_rate = None
        self._seller_user_type = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def application_info(self):
        return self._application_info

    @application_info.setter
    def application_info(self, value):
        if isinstance(value, InsOpenApplicationInfoDTO):
            self._application_info = value
        else:
            self._application_info = InsOpenApplicationInfoDTO.from_alipay_dict(value)
    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value
    @property
    def bank_card_holder_name(self):
        return self._bank_card_holder_name

    @bank_card_holder_name.setter
    def bank_card_holder_name(self, value):
        self._bank_card_holder_name = value
    @property
    def bank_card_no(self):
        return self._bank_card_no

    @bank_card_no.setter
    def bank_card_no(self, value):
        self._bank_card_no = value
    @property
    def bank_id(self):
        return self._bank_id

    @bank_id.setter
    def bank_id(self, value):
        self._bank_id = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def bill_account_type(self):
        return self._bill_account_type

    @bill_account_type.setter
    def bill_account_type(self, value):
        self._bill_account_type = value
    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def id_card_type(self):
        return self._id_card_type

    @id_card_type.setter
    def id_card_type(self, value):
        self._id_card_type = value
    @property
    def main_cat_order_count_of_platform(self):
        return self._main_cat_order_count_of_platform

    @main_cat_order_count_of_platform.setter
    def main_cat_order_count_of_platform(self, value):
        self._main_cat_order_count_of_platform = value
    @property
    def main_cat_refund_exchange_rate_of_platform(self):
        return self._main_cat_refund_exchange_rate_of_platform

    @main_cat_refund_exchange_rate_of_platform.setter
    def main_cat_refund_exchange_rate_of_platform(self, value):
        self._main_cat_refund_exchange_rate_of_platform = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def seller_nick(self):
        return self._seller_nick

    @seller_nick.setter
    def seller_nick(self, value):
        self._seller_nick = value
    @property
    def seller_order_count(self):
        return self._seller_order_count

    @seller_order_count.setter
    def seller_order_count(self, value):
        self._seller_order_count = value
    @property
    def seller_order_refund_exchange_rate(self):
        return self._seller_order_refund_exchange_rate

    @seller_order_refund_exchange_rate.setter
    def seller_order_refund_exchange_rate(self, value):
        self._seller_order_refund_exchange_rate = value
    @property
    def seller_user_type(self):
        return self._seller_user_type

    @seller_user_type.setter
    def seller_user_type(self, value):
        self._seller_user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.application_info:
            if hasattr(self.application_info, 'to_alipay_dict'):
                params['application_info'] = self.application_info.to_alipay_dict()
            else:
                params['application_info'] = self.application_info
        if self.attributes:
            if hasattr(self.attributes, 'to_alipay_dict'):
                params['attributes'] = self.attributes.to_alipay_dict()
            else:
                params['attributes'] = self.attributes
        if self.bank_card_holder_name:
            if hasattr(self.bank_card_holder_name, 'to_alipay_dict'):
                params['bank_card_holder_name'] = self.bank_card_holder_name.to_alipay_dict()
            else:
                params['bank_card_holder_name'] = self.bank_card_holder_name
        if self.bank_card_no:
            if hasattr(self.bank_card_no, 'to_alipay_dict'):
                params['bank_card_no'] = self.bank_card_no.to_alipay_dict()
            else:
                params['bank_card_no'] = self.bank_card_no
        if self.bank_id:
            if hasattr(self.bank_id, 'to_alipay_dict'):
                params['bank_id'] = self.bank_id.to_alipay_dict()
            else:
                params['bank_id'] = self.bank_id
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.bill_account_type:
            if hasattr(self.bill_account_type, 'to_alipay_dict'):
                params['bill_account_type'] = self.bill_account_type.to_alipay_dict()
            else:
                params['bill_account_type'] = self.bill_account_type
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.id_card_type:
            if hasattr(self.id_card_type, 'to_alipay_dict'):
                params['id_card_type'] = self.id_card_type.to_alipay_dict()
            else:
                params['id_card_type'] = self.id_card_type
        if self.main_cat_order_count_of_platform:
            if hasattr(self.main_cat_order_count_of_platform, 'to_alipay_dict'):
                params['main_cat_order_count_of_platform'] = self.main_cat_order_count_of_platform.to_alipay_dict()
            else:
                params['main_cat_order_count_of_platform'] = self.main_cat_order_count_of_platform
        if self.main_cat_refund_exchange_rate_of_platform:
            if hasattr(self.main_cat_refund_exchange_rate_of_platform, 'to_alipay_dict'):
                params['main_cat_refund_exchange_rate_of_platform'] = self.main_cat_refund_exchange_rate_of_platform.to_alipay_dict()
            else:
                params['main_cat_refund_exchange_rate_of_platform'] = self.main_cat_refund_exchange_rate_of_platform
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.seller_nick:
            if hasattr(self.seller_nick, 'to_alipay_dict'):
                params['seller_nick'] = self.seller_nick.to_alipay_dict()
            else:
                params['seller_nick'] = self.seller_nick
        if self.seller_order_count:
            if hasattr(self.seller_order_count, 'to_alipay_dict'):
                params['seller_order_count'] = self.seller_order_count.to_alipay_dict()
            else:
                params['seller_order_count'] = self.seller_order_count
        if self.seller_order_refund_exchange_rate:
            if hasattr(self.seller_order_refund_exchange_rate, 'to_alipay_dict'):
                params['seller_order_refund_exchange_rate'] = self.seller_order_refund_exchange_rate.to_alipay_dict()
            else:
                params['seller_order_refund_exchange_rate'] = self.seller_order_refund_exchange_rate
        if self.seller_user_type:
            if hasattr(self.seller_user_type, 'to_alipay_dict'):
                params['seller_user_type'] = self.seller_user_type.to_alipay_dict()
            else:
                params['seller_user_type'] = self.seller_user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomSellerDTO()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'application_info' in d:
            o.application_info = d['application_info']
        if 'attributes' in d:
            o.attributes = d['attributes']
        if 'bank_card_holder_name' in d:
            o.bank_card_holder_name = d['bank_card_holder_name']
        if 'bank_card_no' in d:
            o.bank_card_no = d['bank_card_no']
        if 'bank_id' in d:
            o.bank_id = d['bank_id']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'bill_account_type' in d:
            o.bill_account_type = d['bill_account_type']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'id_card_type' in d:
            o.id_card_type = d['id_card_type']
        if 'main_cat_order_count_of_platform' in d:
            o.main_cat_order_count_of_platform = d['main_cat_order_count_of_platform']
        if 'main_cat_refund_exchange_rate_of_platform' in d:
            o.main_cat_refund_exchange_rate_of_platform = d['main_cat_refund_exchange_rate_of_platform']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'seller_nick' in d:
            o.seller_nick = d['seller_nick']
        if 'seller_order_count' in d:
            o.seller_order_count = d['seller_order_count']
        if 'seller_order_refund_exchange_rate' in d:
            o.seller_order_refund_exchange_rate = d['seller_order_refund_exchange_rate']
        if 'seller_user_type' in d:
            o.seller_user_type = d['seller_user_type']
        return o



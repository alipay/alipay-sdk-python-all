#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcomBuyerDTO(object):

    def __init__(self):
        self._address = None
        self._alipay_id = None
        self._alipay_logon_id = None
        self._alipay_open_id = None
        self._bank_card_holder_name = None
        self._bank_card_no = None
        self._bank_id = None
        self._bank_name = None
        self._bill_account_type = None
        self._buyer_id = None
        self._buyer_nick = None
        self._buyer_order_count = None
        self._buyer_order_refund_exchange_rate = None
        self._buyer_tag_data = None
        self._id_card_no = None
        self._id_card_type = None
        self._phone = None
        self._real_name = None
        self._user_type = None

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
    def alipay_logon_id(self):
        return self._alipay_logon_id

    @alipay_logon_id.setter
    def alipay_logon_id(self, value):
        self._alipay_logon_id = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
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
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, value):
        self._buyer_nick = value
    @property
    def buyer_order_count(self):
        return self._buyer_order_count

    @buyer_order_count.setter
    def buyer_order_count(self, value):
        self._buyer_order_count = value
    @property
    def buyer_order_refund_exchange_rate(self):
        return self._buyer_order_refund_exchange_rate

    @buyer_order_refund_exchange_rate.setter
    def buyer_order_refund_exchange_rate(self, value):
        self._buyer_order_refund_exchange_rate = value
    @property
    def buyer_tag_data(self):
        return self._buyer_tag_data

    @buyer_tag_data.setter
    def buyer_tag_data(self, value):
        self._buyer_tag_data = value
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
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


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
        if self.alipay_logon_id:
            if hasattr(self.alipay_logon_id, 'to_alipay_dict'):
                params['alipay_logon_id'] = self.alipay_logon_id.to_alipay_dict()
            else:
                params['alipay_logon_id'] = self.alipay_logon_id
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
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
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_nick:
            if hasattr(self.buyer_nick, 'to_alipay_dict'):
                params['buyer_nick'] = self.buyer_nick.to_alipay_dict()
            else:
                params['buyer_nick'] = self.buyer_nick
        if self.buyer_order_count:
            if hasattr(self.buyer_order_count, 'to_alipay_dict'):
                params['buyer_order_count'] = self.buyer_order_count.to_alipay_dict()
            else:
                params['buyer_order_count'] = self.buyer_order_count
        if self.buyer_order_refund_exchange_rate:
            if hasattr(self.buyer_order_refund_exchange_rate, 'to_alipay_dict'):
                params['buyer_order_refund_exchange_rate'] = self.buyer_order_refund_exchange_rate.to_alipay_dict()
            else:
                params['buyer_order_refund_exchange_rate'] = self.buyer_order_refund_exchange_rate
        if self.buyer_tag_data:
            if hasattr(self.buyer_tag_data, 'to_alipay_dict'):
                params['buyer_tag_data'] = self.buyer_tag_data.to_alipay_dict()
            else:
                params['buyer_tag_data'] = self.buyer_tag_data
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
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcomBuyerDTO()
        if 'address' in d:
            o.address = d['address']
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'alipay_logon_id' in d:
            o.alipay_logon_id = d['alipay_logon_id']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
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
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_nick' in d:
            o.buyer_nick = d['buyer_nick']
        if 'buyer_order_count' in d:
            o.buyer_order_count = d['buyer_order_count']
        if 'buyer_order_refund_exchange_rate' in d:
            o.buyer_order_refund_exchange_rate = d['buyer_order_refund_exchange_rate']
        if 'buyer_tag_data' in d:
            o.buyer_tag_data = d['buyer_tag_data']
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'id_card_type' in d:
            o.id_card_type = d['id_card_type']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o



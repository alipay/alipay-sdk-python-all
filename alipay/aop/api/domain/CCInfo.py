#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CCInfo(object):

    def __init__(self):
        self._address = None
        self._cc_ext = None
        self._cr_code = None
        self._cr_desc = None
        self._email = None
        self._item_alias_name = None
        self._item_desc = None
        self._item_id = None
        self._item_name = None
        self._quantity = None
        self._recipient_entity_name = None
        self._recipient_name = None
        self._recipient_phone = None
        self._unit_price = None
        self._zip_code = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def cc_ext(self):
        return self._cc_ext

    @cc_ext.setter
    def cc_ext(self, value):
        self._cc_ext = value
    @property
    def cr_code(self):
        return self._cr_code

    @cr_code.setter
    def cr_code(self, value):
        self._cr_code = value
    @property
    def cr_desc(self):
        return self._cr_desc

    @cr_desc.setter
    def cr_desc(self, value):
        self._cr_desc = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def item_alias_name(self):
        return self._item_alias_name

    @item_alias_name.setter
    def item_alias_name(self, value):
        self._item_alias_name = value
    @property
    def item_desc(self):
        return self._item_desc

    @item_desc.setter
    def item_desc(self, value):
        self._item_desc = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def recipient_entity_name(self):
        return self._recipient_entity_name

    @recipient_entity_name.setter
    def recipient_entity_name(self, value):
        self._recipient_entity_name = value
    @property
    def recipient_name(self):
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, value):
        self._recipient_name = value
    @property
    def recipient_phone(self):
        return self._recipient_phone

    @recipient_phone.setter
    def recipient_phone(self, value):
        self._recipient_phone = value
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.cc_ext:
            if hasattr(self.cc_ext, 'to_alipay_dict'):
                params['cc_ext'] = self.cc_ext.to_alipay_dict()
            else:
                params['cc_ext'] = self.cc_ext
        if self.cr_code:
            if hasattr(self.cr_code, 'to_alipay_dict'):
                params['cr_code'] = self.cr_code.to_alipay_dict()
            else:
                params['cr_code'] = self.cr_code
        if self.cr_desc:
            if hasattr(self.cr_desc, 'to_alipay_dict'):
                params['cr_desc'] = self.cr_desc.to_alipay_dict()
            else:
                params['cr_desc'] = self.cr_desc
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.item_alias_name:
            if hasattr(self.item_alias_name, 'to_alipay_dict'):
                params['item_alias_name'] = self.item_alias_name.to_alipay_dict()
            else:
                params['item_alias_name'] = self.item_alias_name
        if self.item_desc:
            if hasattr(self.item_desc, 'to_alipay_dict'):
                params['item_desc'] = self.item_desc.to_alipay_dict()
            else:
                params['item_desc'] = self.item_desc
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.recipient_entity_name:
            if hasattr(self.recipient_entity_name, 'to_alipay_dict'):
                params['recipient_entity_name'] = self.recipient_entity_name.to_alipay_dict()
            else:
                params['recipient_entity_name'] = self.recipient_entity_name
        if self.recipient_name:
            if hasattr(self.recipient_name, 'to_alipay_dict'):
                params['recipient_name'] = self.recipient_name.to_alipay_dict()
            else:
                params['recipient_name'] = self.recipient_name
        if self.recipient_phone:
            if hasattr(self.recipient_phone, 'to_alipay_dict'):
                params['recipient_phone'] = self.recipient_phone.to_alipay_dict()
            else:
                params['recipient_phone'] = self.recipient_phone
        if self.unit_price:
            if hasattr(self.unit_price, 'to_alipay_dict'):
                params['unit_price'] = self.unit_price.to_alipay_dict()
            else:
                params['unit_price'] = self.unit_price
        if self.zip_code:
            if hasattr(self.zip_code, 'to_alipay_dict'):
                params['zip_code'] = self.zip_code.to_alipay_dict()
            else:
                params['zip_code'] = self.zip_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CCInfo()
        if 'address' in d:
            o.address = d['address']
        if 'cc_ext' in d:
            o.cc_ext = d['cc_ext']
        if 'cr_code' in d:
            o.cr_code = d['cr_code']
        if 'cr_desc' in d:
            o.cr_desc = d['cr_desc']
        if 'email' in d:
            o.email = d['email']
        if 'item_alias_name' in d:
            o.item_alias_name = d['item_alias_name']
        if 'item_desc' in d:
            o.item_desc = d['item_desc']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'recipient_entity_name' in d:
            o.recipient_entity_name = d['recipient_entity_name']
        if 'recipient_name' in d:
            o.recipient_name = d['recipient_name']
        if 'recipient_phone' in d:
            o.recipient_phone = d['recipient_phone']
        if 'unit_price' in d:
            o.unit_price = d['unit_price']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o



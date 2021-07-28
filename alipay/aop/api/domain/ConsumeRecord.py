#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundItem import FundItem


class ConsumeRecord(object):

    def __init__(self):
        self._alipay_order_no = None
        self._biz_state = None
        self._biz_state_desc = None
        self._consume_fee = None
        self._delete_type = None
        self._fund_items = None
        self._gmt_biz_create = None
        self._gmt_biz_modified = None
        self._in_out = None
        self._merchant_order_no = None
        self._opposite_logo = None
        self._opposite_name = None
        self._owner_card_no = None
        self._owner_logon_id = None
        self._owner_name = None
        self._refund = None

    @property
    def alipay_order_no(self):
        return self._alipay_order_no

    @alipay_order_no.setter
    def alipay_order_no(self, value):
        self._alipay_order_no = value
    @property
    def biz_state(self):
        return self._biz_state

    @biz_state.setter
    def biz_state(self, value):
        self._biz_state = value
    @property
    def biz_state_desc(self):
        return self._biz_state_desc

    @biz_state_desc.setter
    def biz_state_desc(self, value):
        self._biz_state_desc = value
    @property
    def consume_fee(self):
        return self._consume_fee

    @consume_fee.setter
    def consume_fee(self, value):
        self._consume_fee = value
    @property
    def delete_type(self):
        return self._delete_type

    @delete_type.setter
    def delete_type(self, value):
        self._delete_type = value
    @property
    def fund_items(self):
        return self._fund_items

    @fund_items.setter
    def fund_items(self, value):
        if isinstance(value, list):
            self._fund_items = list()
            for i in value:
                if isinstance(i, FundItem):
                    self._fund_items.append(i)
                else:
                    self._fund_items.append(FundItem.from_alipay_dict(i))
    @property
    def gmt_biz_create(self):
        return self._gmt_biz_create

    @gmt_biz_create.setter
    def gmt_biz_create(self, value):
        self._gmt_biz_create = value
    @property
    def gmt_biz_modified(self):
        return self._gmt_biz_modified

    @gmt_biz_modified.setter
    def gmt_biz_modified(self, value):
        self._gmt_biz_modified = value
    @property
    def in_out(self):
        return self._in_out

    @in_out.setter
    def in_out(self, value):
        self._in_out = value
    @property
    def merchant_order_no(self):
        return self._merchant_order_no

    @merchant_order_no.setter
    def merchant_order_no(self, value):
        self._merchant_order_no = value
    @property
    def opposite_logo(self):
        return self._opposite_logo

    @opposite_logo.setter
    def opposite_logo(self, value):
        self._opposite_logo = value
    @property
    def opposite_name(self):
        return self._opposite_name

    @opposite_name.setter
    def opposite_name(self, value):
        self._opposite_name = value
    @property
    def owner_card_no(self):
        return self._owner_card_no

    @owner_card_no.setter
    def owner_card_no(self, value):
        self._owner_card_no = value
    @property
    def owner_logon_id(self):
        return self._owner_logon_id

    @owner_logon_id.setter
    def owner_logon_id(self, value):
        self._owner_logon_id = value
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value
    @property
    def refund(self):
        return self._refund

    @refund.setter
    def refund(self, value):
        self._refund = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_no:
            if hasattr(self.alipay_order_no, 'to_alipay_dict'):
                params['alipay_order_no'] = self.alipay_order_no.to_alipay_dict()
            else:
                params['alipay_order_no'] = self.alipay_order_no
        if self.biz_state:
            if hasattr(self.biz_state, 'to_alipay_dict'):
                params['biz_state'] = self.biz_state.to_alipay_dict()
            else:
                params['biz_state'] = self.biz_state
        if self.biz_state_desc:
            if hasattr(self.biz_state_desc, 'to_alipay_dict'):
                params['biz_state_desc'] = self.biz_state_desc.to_alipay_dict()
            else:
                params['biz_state_desc'] = self.biz_state_desc
        if self.consume_fee:
            if hasattr(self.consume_fee, 'to_alipay_dict'):
                params['consume_fee'] = self.consume_fee.to_alipay_dict()
            else:
                params['consume_fee'] = self.consume_fee
        if self.delete_type:
            if hasattr(self.delete_type, 'to_alipay_dict'):
                params['delete_type'] = self.delete_type.to_alipay_dict()
            else:
                params['delete_type'] = self.delete_type
        if self.fund_items:
            if isinstance(self.fund_items, list):
                for i in range(0, len(self.fund_items)):
                    element = self.fund_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_items[i] = element.to_alipay_dict()
            if hasattr(self.fund_items, 'to_alipay_dict'):
                params['fund_items'] = self.fund_items.to_alipay_dict()
            else:
                params['fund_items'] = self.fund_items
        if self.gmt_biz_create:
            if hasattr(self.gmt_biz_create, 'to_alipay_dict'):
                params['gmt_biz_create'] = self.gmt_biz_create.to_alipay_dict()
            else:
                params['gmt_biz_create'] = self.gmt_biz_create
        if self.gmt_biz_modified:
            if hasattr(self.gmt_biz_modified, 'to_alipay_dict'):
                params['gmt_biz_modified'] = self.gmt_biz_modified.to_alipay_dict()
            else:
                params['gmt_biz_modified'] = self.gmt_biz_modified
        if self.in_out:
            if hasattr(self.in_out, 'to_alipay_dict'):
                params['in_out'] = self.in_out.to_alipay_dict()
            else:
                params['in_out'] = self.in_out
        if self.merchant_order_no:
            if hasattr(self.merchant_order_no, 'to_alipay_dict'):
                params['merchant_order_no'] = self.merchant_order_no.to_alipay_dict()
            else:
                params['merchant_order_no'] = self.merchant_order_no
        if self.opposite_logo:
            if hasattr(self.opposite_logo, 'to_alipay_dict'):
                params['opposite_logo'] = self.opposite_logo.to_alipay_dict()
            else:
                params['opposite_logo'] = self.opposite_logo
        if self.opposite_name:
            if hasattr(self.opposite_name, 'to_alipay_dict'):
                params['opposite_name'] = self.opposite_name.to_alipay_dict()
            else:
                params['opposite_name'] = self.opposite_name
        if self.owner_card_no:
            if hasattr(self.owner_card_no, 'to_alipay_dict'):
                params['owner_card_no'] = self.owner_card_no.to_alipay_dict()
            else:
                params['owner_card_no'] = self.owner_card_no
        if self.owner_logon_id:
            if hasattr(self.owner_logon_id, 'to_alipay_dict'):
                params['owner_logon_id'] = self.owner_logon_id.to_alipay_dict()
            else:
                params['owner_logon_id'] = self.owner_logon_id
        if self.owner_name:
            if hasattr(self.owner_name, 'to_alipay_dict'):
                params['owner_name'] = self.owner_name.to_alipay_dict()
            else:
                params['owner_name'] = self.owner_name
        if self.refund:
            if hasattr(self.refund, 'to_alipay_dict'):
                params['refund'] = self.refund.to_alipay_dict()
            else:
                params['refund'] = self.refund
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumeRecord()
        if 'alipay_order_no' in d:
            o.alipay_order_no = d['alipay_order_no']
        if 'biz_state' in d:
            o.biz_state = d['biz_state']
        if 'biz_state_desc' in d:
            o.biz_state_desc = d['biz_state_desc']
        if 'consume_fee' in d:
            o.consume_fee = d['consume_fee']
        if 'delete_type' in d:
            o.delete_type = d['delete_type']
        if 'fund_items' in d:
            o.fund_items = d['fund_items']
        if 'gmt_biz_create' in d:
            o.gmt_biz_create = d['gmt_biz_create']
        if 'gmt_biz_modified' in d:
            o.gmt_biz_modified = d['gmt_biz_modified']
        if 'in_out' in d:
            o.in_out = d['in_out']
        if 'merchant_order_no' in d:
            o.merchant_order_no = d['merchant_order_no']
        if 'opposite_logo' in d:
            o.opposite_logo = d['opposite_logo']
        if 'opposite_name' in d:
            o.opposite_name = d['opposite_name']
        if 'owner_card_no' in d:
            o.owner_card_no = d['owner_card_no']
        if 'owner_logon_id' in d:
            o.owner_logon_id = d['owner_logon_id']
        if 'owner_name' in d:
            o.owner_name = d['owner_name']
        if 'refund' in d:
            o.refund = d['refund']
        return o



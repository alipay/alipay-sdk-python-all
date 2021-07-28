#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCashlessticketTemplateCreateModel(object):

    def __init__(self):
        self._amount = None
        self._brand_name = None
        self._extension_info = None
        self._group_code = None
        self._memo = None
        self._notify_uri = None
        self._out_biz_no = None
        self._publish_end_time = None
        self._publish_start_time = None
        self._rule_conf = None
        self._ticket_available_time = None
        self._ticket_description = None
        self._ticket_quantity = None
        self._ticket_type = None
        self._ticket_valid_period = None
        self._total_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def extension_info(self):
        return self._extension_info

    @extension_info.setter
    def extension_info(self, value):
        self._extension_info = value
    @property
    def group_code(self):
        return self._group_code

    @group_code.setter
    def group_code(self, value):
        self._group_code = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def notify_uri(self):
        return self._notify_uri

    @notify_uri.setter
    def notify_uri(self, value):
        self._notify_uri = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value
    @property
    def publish_start_time(self):
        return self._publish_start_time

    @publish_start_time.setter
    def publish_start_time(self, value):
        self._publish_start_time = value
    @property
    def rule_conf(self):
        return self._rule_conf

    @rule_conf.setter
    def rule_conf(self, value):
        self._rule_conf = value
    @property
    def ticket_available_time(self):
        return self._ticket_available_time

    @ticket_available_time.setter
    def ticket_available_time(self, value):
        self._ticket_available_time = value
    @property
    def ticket_description(self):
        return self._ticket_description

    @ticket_description.setter
    def ticket_description(self, value):
        self._ticket_description = value
    @property
    def ticket_quantity(self):
        return self._ticket_quantity

    @ticket_quantity.setter
    def ticket_quantity(self, value):
        self._ticket_quantity = value
    @property
    def ticket_type(self):
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, value):
        self._ticket_type = value
    @property
    def ticket_valid_period(self):
        return self._ticket_valid_period

    @ticket_valid_period.setter
    def ticket_valid_period(self, value):
        self._ticket_valid_period = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.extension_info:
            if hasattr(self.extension_info, 'to_alipay_dict'):
                params['extension_info'] = self.extension_info.to_alipay_dict()
            else:
                params['extension_info'] = self.extension_info
        if self.group_code:
            if hasattr(self.group_code, 'to_alipay_dict'):
                params['group_code'] = self.group_code.to_alipay_dict()
            else:
                params['group_code'] = self.group_code
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.notify_uri:
            if hasattr(self.notify_uri, 'to_alipay_dict'):
                params['notify_uri'] = self.notify_uri.to_alipay_dict()
            else:
                params['notify_uri'] = self.notify_uri
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.publish_end_time:
            if hasattr(self.publish_end_time, 'to_alipay_dict'):
                params['publish_end_time'] = self.publish_end_time.to_alipay_dict()
            else:
                params['publish_end_time'] = self.publish_end_time
        if self.publish_start_time:
            if hasattr(self.publish_start_time, 'to_alipay_dict'):
                params['publish_start_time'] = self.publish_start_time.to_alipay_dict()
            else:
                params['publish_start_time'] = self.publish_start_time
        if self.rule_conf:
            if hasattr(self.rule_conf, 'to_alipay_dict'):
                params['rule_conf'] = self.rule_conf.to_alipay_dict()
            else:
                params['rule_conf'] = self.rule_conf
        if self.ticket_available_time:
            if hasattr(self.ticket_available_time, 'to_alipay_dict'):
                params['ticket_available_time'] = self.ticket_available_time.to_alipay_dict()
            else:
                params['ticket_available_time'] = self.ticket_available_time
        if self.ticket_description:
            if hasattr(self.ticket_description, 'to_alipay_dict'):
                params['ticket_description'] = self.ticket_description.to_alipay_dict()
            else:
                params['ticket_description'] = self.ticket_description
        if self.ticket_quantity:
            if hasattr(self.ticket_quantity, 'to_alipay_dict'):
                params['ticket_quantity'] = self.ticket_quantity.to_alipay_dict()
            else:
                params['ticket_quantity'] = self.ticket_quantity
        if self.ticket_type:
            if hasattr(self.ticket_type, 'to_alipay_dict'):
                params['ticket_type'] = self.ticket_type.to_alipay_dict()
            else:
                params['ticket_type'] = self.ticket_type
        if self.ticket_valid_period:
            if hasattr(self.ticket_valid_period, 'to_alipay_dict'):
                params['ticket_valid_period'] = self.ticket_valid_period.to_alipay_dict()
            else:
                params['ticket_valid_period'] = self.ticket_valid_period
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCashlessticketTemplateCreateModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'extension_info' in d:
            o.extension_info = d['extension_info']
        if 'group_code' in d:
            o.group_code = d['group_code']
        if 'memo' in d:
            o.memo = d['memo']
        if 'notify_uri' in d:
            o.notify_uri = d['notify_uri']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'publish_end_time' in d:
            o.publish_end_time = d['publish_end_time']
        if 'publish_start_time' in d:
            o.publish_start_time = d['publish_start_time']
        if 'rule_conf' in d:
            o.rule_conf = d['rule_conf']
        if 'ticket_available_time' in d:
            o.ticket_available_time = d['ticket_available_time']
        if 'ticket_description' in d:
            o.ticket_description = d['ticket_description']
        if 'ticket_quantity' in d:
            o.ticket_quantity = d['ticket_quantity']
        if 'ticket_type' in d:
            o.ticket_type = d['ticket_type']
        if 'ticket_valid_period' in d:
            o.ticket_valid_period = d['ticket_valid_period']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



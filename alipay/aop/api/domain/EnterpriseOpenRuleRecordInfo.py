#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EnterpriseOpenRuleRecordInfo(object):

    def __init__(self):
        self._bill_month_day = None
        self._bill_scope = None
        self._combined_pay_mode = None
        self._default_invoice_kind = None
        self._effective_start = None
        self._enterprise_id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._invoice_remark_value_rule = None
        self._invoice_rule_id = None
        self._invoice_rule_record_id = None
        self._invoice_title_id = None
        self._open_applyer = None
        self._open_mode = None
        self._open_type = None
        self._owner_id = None
        self._tag = None

    @property
    def bill_month_day(self):
        return self._bill_month_day

    @bill_month_day.setter
    def bill_month_day(self, value):
        self._bill_month_day = value
    @property
    def bill_scope(self):
        return self._bill_scope

    @bill_scope.setter
    def bill_scope(self, value):
        self._bill_scope = value
    @property
    def combined_pay_mode(self):
        return self._combined_pay_mode

    @combined_pay_mode.setter
    def combined_pay_mode(self, value):
        self._combined_pay_mode = value
    @property
    def default_invoice_kind(self):
        return self._default_invoice_kind

    @default_invoice_kind.setter
    def default_invoice_kind(self, value):
        self._default_invoice_kind = value
    @property
    def effective_start(self):
        return self._effective_start

    @effective_start.setter
    def effective_start(self, value):
        self._effective_start = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def invoice_remark_value_rule(self):
        return self._invoice_remark_value_rule

    @invoice_remark_value_rule.setter
    def invoice_remark_value_rule(self, value):
        self._invoice_remark_value_rule = value
    @property
    def invoice_rule_id(self):
        return self._invoice_rule_id

    @invoice_rule_id.setter
    def invoice_rule_id(self, value):
        self._invoice_rule_id = value
    @property
    def invoice_rule_record_id(self):
        return self._invoice_rule_record_id

    @invoice_rule_record_id.setter
    def invoice_rule_record_id(self, value):
        self._invoice_rule_record_id = value
    @property
    def invoice_title_id(self):
        return self._invoice_title_id

    @invoice_title_id.setter
    def invoice_title_id(self, value):
        self._invoice_title_id = value
    @property
    def open_applyer(self):
        return self._open_applyer

    @open_applyer.setter
    def open_applyer(self, value):
        self._open_applyer = value
    @property
    def open_mode(self):
        return self._open_mode

    @open_mode.setter
    def open_mode(self, value):
        self._open_mode = value
    @property
    def open_type(self):
        return self._open_type

    @open_type.setter
    def open_type(self, value):
        self._open_type = value
    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        self._owner_id = value
    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_month_day:
            if hasattr(self.bill_month_day, 'to_alipay_dict'):
                params['bill_month_day'] = self.bill_month_day.to_alipay_dict()
            else:
                params['bill_month_day'] = self.bill_month_day
        if self.bill_scope:
            if hasattr(self.bill_scope, 'to_alipay_dict'):
                params['bill_scope'] = self.bill_scope.to_alipay_dict()
            else:
                params['bill_scope'] = self.bill_scope
        if self.combined_pay_mode:
            if hasattr(self.combined_pay_mode, 'to_alipay_dict'):
                params['combined_pay_mode'] = self.combined_pay_mode.to_alipay_dict()
            else:
                params['combined_pay_mode'] = self.combined_pay_mode
        if self.default_invoice_kind:
            if hasattr(self.default_invoice_kind, 'to_alipay_dict'):
                params['default_invoice_kind'] = self.default_invoice_kind.to_alipay_dict()
            else:
                params['default_invoice_kind'] = self.default_invoice_kind
        if self.effective_start:
            if hasattr(self.effective_start, 'to_alipay_dict'):
                params['effective_start'] = self.effective_start.to_alipay_dict()
            else:
                params['effective_start'] = self.effective_start
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.invoice_remark_value_rule:
            if hasattr(self.invoice_remark_value_rule, 'to_alipay_dict'):
                params['invoice_remark_value_rule'] = self.invoice_remark_value_rule.to_alipay_dict()
            else:
                params['invoice_remark_value_rule'] = self.invoice_remark_value_rule
        if self.invoice_rule_id:
            if hasattr(self.invoice_rule_id, 'to_alipay_dict'):
                params['invoice_rule_id'] = self.invoice_rule_id.to_alipay_dict()
            else:
                params['invoice_rule_id'] = self.invoice_rule_id
        if self.invoice_rule_record_id:
            if hasattr(self.invoice_rule_record_id, 'to_alipay_dict'):
                params['invoice_rule_record_id'] = self.invoice_rule_record_id.to_alipay_dict()
            else:
                params['invoice_rule_record_id'] = self.invoice_rule_record_id
        if self.invoice_title_id:
            if hasattr(self.invoice_title_id, 'to_alipay_dict'):
                params['invoice_title_id'] = self.invoice_title_id.to_alipay_dict()
            else:
                params['invoice_title_id'] = self.invoice_title_id
        if self.open_applyer:
            if hasattr(self.open_applyer, 'to_alipay_dict'):
                params['open_applyer'] = self.open_applyer.to_alipay_dict()
            else:
                params['open_applyer'] = self.open_applyer
        if self.open_mode:
            if hasattr(self.open_mode, 'to_alipay_dict'):
                params['open_mode'] = self.open_mode.to_alipay_dict()
            else:
                params['open_mode'] = self.open_mode
        if self.open_type:
            if hasattr(self.open_type, 'to_alipay_dict'):
                params['open_type'] = self.open_type.to_alipay_dict()
            else:
                params['open_type'] = self.open_type
        if self.owner_id:
            if hasattr(self.owner_id, 'to_alipay_dict'):
                params['owner_id'] = self.owner_id.to_alipay_dict()
            else:
                params['owner_id'] = self.owner_id
        if self.tag:
            if hasattr(self.tag, 'to_alipay_dict'):
                params['tag'] = self.tag.to_alipay_dict()
            else:
                params['tag'] = self.tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EnterpriseOpenRuleRecordInfo()
        if 'bill_month_day' in d:
            o.bill_month_day = d['bill_month_day']
        if 'bill_scope' in d:
            o.bill_scope = d['bill_scope']
        if 'combined_pay_mode' in d:
            o.combined_pay_mode = d['combined_pay_mode']
        if 'default_invoice_kind' in d:
            o.default_invoice_kind = d['default_invoice_kind']
        if 'effective_start' in d:
            o.effective_start = d['effective_start']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'invoice_remark_value_rule' in d:
            o.invoice_remark_value_rule = d['invoice_remark_value_rule']
        if 'invoice_rule_id' in d:
            o.invoice_rule_id = d['invoice_rule_id']
        if 'invoice_rule_record_id' in d:
            o.invoice_rule_record_id = d['invoice_rule_record_id']
        if 'invoice_title_id' in d:
            o.invoice_title_id = d['invoice_title_id']
        if 'open_applyer' in d:
            o.open_applyer = d['open_applyer']
        if 'open_mode' in d:
            o.open_mode = d['open_mode']
        if 'open_type' in d:
            o.open_type = d['open_type']
        if 'owner_id' in d:
            o.owner_id = d['owner_id']
        if 'tag' in d:
            o.tag = d['tag']
        return o



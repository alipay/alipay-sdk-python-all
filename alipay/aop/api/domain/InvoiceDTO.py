#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceDTO(object):

    def __init__(self):
        self._amount = None
        self._approve_date = None
        self._approved_by = None
        self._archive_no = None
        self._archive_status = None
        self._biz_id = None
        self._confirm_date = None
        self._confirm_way = None
        self._create_date = None
        self._currency = None
        self._desc_status = None
        self._discard_amount = None
        self._distribute_invoice_id = None
        self._effect_status = None
        self._entry_date = None
        self._entry_user = None
        self._excluding_tax_amount = None
        self._ext_json = None
        self._invoice_date = None
        self._invoice_id = None
        self._invoice_no = None
        self._invoice_status = None
        self._invoice_type = None
        self._org_id = None
        self._ou_code = None
        self._red = None
        self._reg_date = None
        self._return_by = None
        self._return_date = None
        self._return_reason = None
        self._source_system = None
        self._source_unique_no = None
        self._tax_amount = None
        self._tax_invoice_id = None
        self._tax_rate = None
        self._tracking_no = None
        self._use_amount = None
        self._vendor_id = None
        self._verify_date = None
        self._verify_period = None
        self._verify_status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def approve_date(self):
        return self._approve_date

    @approve_date.setter
    def approve_date(self, value):
        self._approve_date = value
    @property
    def approved_by(self):
        return self._approved_by

    @approved_by.setter
    def approved_by(self, value):
        self._approved_by = value
    @property
    def archive_no(self):
        return self._archive_no

    @archive_no.setter
    def archive_no(self, value):
        self._archive_no = value
    @property
    def archive_status(self):
        return self._archive_status

    @archive_status.setter
    def archive_status(self, value):
        self._archive_status = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def confirm_date(self):
        return self._confirm_date

    @confirm_date.setter
    def confirm_date(self, value):
        self._confirm_date = value
    @property
    def confirm_way(self):
        return self._confirm_way

    @confirm_way.setter
    def confirm_way(self, value):
        self._confirm_way = value
    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def desc_status(self):
        return self._desc_status

    @desc_status.setter
    def desc_status(self, value):
        self._desc_status = value
    @property
    def discard_amount(self):
        return self._discard_amount

    @discard_amount.setter
    def discard_amount(self, value):
        self._discard_amount = value
    @property
    def distribute_invoice_id(self):
        return self._distribute_invoice_id

    @distribute_invoice_id.setter
    def distribute_invoice_id(self, value):
        self._distribute_invoice_id = value
    @property
    def effect_status(self):
        return self._effect_status

    @effect_status.setter
    def effect_status(self, value):
        self._effect_status = value
    @property
    def entry_date(self):
        return self._entry_date

    @entry_date.setter
    def entry_date(self, value):
        self._entry_date = value
    @property
    def entry_user(self):
        return self._entry_user

    @entry_user.setter
    def entry_user(self, value):
        self._entry_user = value
    @property
    def excluding_tax_amount(self):
        return self._excluding_tax_amount

    @excluding_tax_amount.setter
    def excluding_tax_amount(self, value):
        self._excluding_tax_amount = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def invoice_date(self):
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, value):
        self._invoice_date = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_no(self):
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, value):
        self._invoice_no = value
    @property
    def invoice_status(self):
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, value):
        self._invoice_status = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value
    @property
    def reg_date(self):
        return self._reg_date

    @reg_date.setter
    def reg_date(self, value):
        self._reg_date = value
    @property
    def return_by(self):
        return self._return_by

    @return_by.setter
    def return_by(self, value):
        self._return_by = value
    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        self._return_date = value
    @property
    def return_reason(self):
        return self._return_reason

    @return_reason.setter
    def return_reason(self, value):
        self._return_reason = value
    @property
    def source_system(self):
        return self._source_system

    @source_system.setter
    def source_system(self, value):
        self._source_system = value
    @property
    def source_unique_no(self):
        return self._source_unique_no

    @source_unique_no.setter
    def source_unique_no(self, value):
        self._source_unique_no = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_invoice_id(self):
        return self._tax_invoice_id

    @tax_invoice_id.setter
    def tax_invoice_id(self, value):
        self._tax_invoice_id = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def vendor_id(self):
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, value):
        self._vendor_id = value
    @property
    def verify_date(self):
        return self._verify_date

    @verify_date.setter
    def verify_date(self, value):
        self._verify_date = value
    @property
    def verify_period(self):
        return self._verify_period

    @verify_period.setter
    def verify_period(self, value):
        self._verify_period = value
    @property
    def verify_status(self):
        return self._verify_status

    @verify_status.setter
    def verify_status(self, value):
        self._verify_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.approve_date:
            if hasattr(self.approve_date, 'to_alipay_dict'):
                params['approve_date'] = self.approve_date.to_alipay_dict()
            else:
                params['approve_date'] = self.approve_date
        if self.approved_by:
            if hasattr(self.approved_by, 'to_alipay_dict'):
                params['approved_by'] = self.approved_by.to_alipay_dict()
            else:
                params['approved_by'] = self.approved_by
        if self.archive_no:
            if hasattr(self.archive_no, 'to_alipay_dict'):
                params['archive_no'] = self.archive_no.to_alipay_dict()
            else:
                params['archive_no'] = self.archive_no
        if self.archive_status:
            if hasattr(self.archive_status, 'to_alipay_dict'):
                params['archive_status'] = self.archive_status.to_alipay_dict()
            else:
                params['archive_status'] = self.archive_status
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.confirm_date:
            if hasattr(self.confirm_date, 'to_alipay_dict'):
                params['confirm_date'] = self.confirm_date.to_alipay_dict()
            else:
                params['confirm_date'] = self.confirm_date
        if self.confirm_way:
            if hasattr(self.confirm_way, 'to_alipay_dict'):
                params['confirm_way'] = self.confirm_way.to_alipay_dict()
            else:
                params['confirm_way'] = self.confirm_way
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.desc_status:
            if hasattr(self.desc_status, 'to_alipay_dict'):
                params['desc_status'] = self.desc_status.to_alipay_dict()
            else:
                params['desc_status'] = self.desc_status
        if self.discard_amount:
            if hasattr(self.discard_amount, 'to_alipay_dict'):
                params['discard_amount'] = self.discard_amount.to_alipay_dict()
            else:
                params['discard_amount'] = self.discard_amount
        if self.distribute_invoice_id:
            if hasattr(self.distribute_invoice_id, 'to_alipay_dict'):
                params['distribute_invoice_id'] = self.distribute_invoice_id.to_alipay_dict()
            else:
                params['distribute_invoice_id'] = self.distribute_invoice_id
        if self.effect_status:
            if hasattr(self.effect_status, 'to_alipay_dict'):
                params['effect_status'] = self.effect_status.to_alipay_dict()
            else:
                params['effect_status'] = self.effect_status
        if self.entry_date:
            if hasattr(self.entry_date, 'to_alipay_dict'):
                params['entry_date'] = self.entry_date.to_alipay_dict()
            else:
                params['entry_date'] = self.entry_date
        if self.entry_user:
            if hasattr(self.entry_user, 'to_alipay_dict'):
                params['entry_user'] = self.entry_user.to_alipay_dict()
            else:
                params['entry_user'] = self.entry_user
        if self.excluding_tax_amount:
            if hasattr(self.excluding_tax_amount, 'to_alipay_dict'):
                params['excluding_tax_amount'] = self.excluding_tax_amount.to_alipay_dict()
            else:
                params['excluding_tax_amount'] = self.excluding_tax_amount
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.invoice_date:
            if hasattr(self.invoice_date, 'to_alipay_dict'):
                params['invoice_date'] = self.invoice_date.to_alipay_dict()
            else:
                params['invoice_date'] = self.invoice_date
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_no:
            if hasattr(self.invoice_no, 'to_alipay_dict'):
                params['invoice_no'] = self.invoice_no.to_alipay_dict()
            else:
                params['invoice_no'] = self.invoice_no
        if self.invoice_status:
            if hasattr(self.invoice_status, 'to_alipay_dict'):
                params['invoice_status'] = self.invoice_status.to_alipay_dict()
            else:
                params['invoice_status'] = self.invoice_status
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.red:
            if hasattr(self.red, 'to_alipay_dict'):
                params['red'] = self.red.to_alipay_dict()
            else:
                params['red'] = self.red
        if self.reg_date:
            if hasattr(self.reg_date, 'to_alipay_dict'):
                params['reg_date'] = self.reg_date.to_alipay_dict()
            else:
                params['reg_date'] = self.reg_date
        if self.return_by:
            if hasattr(self.return_by, 'to_alipay_dict'):
                params['return_by'] = self.return_by.to_alipay_dict()
            else:
                params['return_by'] = self.return_by
        if self.return_date:
            if hasattr(self.return_date, 'to_alipay_dict'):
                params['return_date'] = self.return_date.to_alipay_dict()
            else:
                params['return_date'] = self.return_date
        if self.return_reason:
            if hasattr(self.return_reason, 'to_alipay_dict'):
                params['return_reason'] = self.return_reason.to_alipay_dict()
            else:
                params['return_reason'] = self.return_reason
        if self.source_system:
            if hasattr(self.source_system, 'to_alipay_dict'):
                params['source_system'] = self.source_system.to_alipay_dict()
            else:
                params['source_system'] = self.source_system
        if self.source_unique_no:
            if hasattr(self.source_unique_no, 'to_alipay_dict'):
                params['source_unique_no'] = self.source_unique_no.to_alipay_dict()
            else:
                params['source_unique_no'] = self.source_unique_no
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_invoice_id:
            if hasattr(self.tax_invoice_id, 'to_alipay_dict'):
                params['tax_invoice_id'] = self.tax_invoice_id.to_alipay_dict()
            else:
                params['tax_invoice_id'] = self.tax_invoice_id
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tracking_no:
            if hasattr(self.tracking_no, 'to_alipay_dict'):
                params['tracking_no'] = self.tracking_no.to_alipay_dict()
            else:
                params['tracking_no'] = self.tracking_no
        if self.use_amount:
            if hasattr(self.use_amount, 'to_alipay_dict'):
                params['use_amount'] = self.use_amount.to_alipay_dict()
            else:
                params['use_amount'] = self.use_amount
        if self.vendor_id:
            if hasattr(self.vendor_id, 'to_alipay_dict'):
                params['vendor_id'] = self.vendor_id.to_alipay_dict()
            else:
                params['vendor_id'] = self.vendor_id
        if self.verify_date:
            if hasattr(self.verify_date, 'to_alipay_dict'):
                params['verify_date'] = self.verify_date.to_alipay_dict()
            else:
                params['verify_date'] = self.verify_date
        if self.verify_period:
            if hasattr(self.verify_period, 'to_alipay_dict'):
                params['verify_period'] = self.verify_period.to_alipay_dict()
            else:
                params['verify_period'] = self.verify_period
        if self.verify_status:
            if hasattr(self.verify_status, 'to_alipay_dict'):
                params['verify_status'] = self.verify_status.to_alipay_dict()
            else:
                params['verify_status'] = self.verify_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'approve_date' in d:
            o.approve_date = d['approve_date']
        if 'approved_by' in d:
            o.approved_by = d['approved_by']
        if 'archive_no' in d:
            o.archive_no = d['archive_no']
        if 'archive_status' in d:
            o.archive_status = d['archive_status']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'confirm_date' in d:
            o.confirm_date = d['confirm_date']
        if 'confirm_way' in d:
            o.confirm_way = d['confirm_way']
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'currency' in d:
            o.currency = d['currency']
        if 'desc_status' in d:
            o.desc_status = d['desc_status']
        if 'discard_amount' in d:
            o.discard_amount = d['discard_amount']
        if 'distribute_invoice_id' in d:
            o.distribute_invoice_id = d['distribute_invoice_id']
        if 'effect_status' in d:
            o.effect_status = d['effect_status']
        if 'entry_date' in d:
            o.entry_date = d['entry_date']
        if 'entry_user' in d:
            o.entry_user = d['entry_user']
        if 'excluding_tax_amount' in d:
            o.excluding_tax_amount = d['excluding_tax_amount']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'invoice_date' in d:
            o.invoice_date = d['invoice_date']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_no' in d:
            o.invoice_no = d['invoice_no']
        if 'invoice_status' in d:
            o.invoice_status = d['invoice_status']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'red' in d:
            o.red = d['red']
        if 'reg_date' in d:
            o.reg_date = d['reg_date']
        if 'return_by' in d:
            o.return_by = d['return_by']
        if 'return_date' in d:
            o.return_date = d['return_date']
        if 'return_reason' in d:
            o.return_reason = d['return_reason']
        if 'source_system' in d:
            o.source_system = d['source_system']
        if 'source_unique_no' in d:
            o.source_unique_no = d['source_unique_no']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_invoice_id' in d:
            o.tax_invoice_id = d['tax_invoice_id']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tracking_no' in d:
            o.tracking_no = d['tracking_no']
        if 'use_amount' in d:
            o.use_amount = d['use_amount']
        if 'vendor_id' in d:
            o.vendor_id = d['vendor_id']
        if 'verify_date' in d:
            o.verify_date = d['verify_date']
        if 'verify_period' in d:
            o.verify_period = d['verify_period']
        if 'verify_status' in d:
            o.verify_status = d['verify_status']
        return o



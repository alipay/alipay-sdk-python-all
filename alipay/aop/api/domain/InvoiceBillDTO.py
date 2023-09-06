#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceBillDTO(object):

    def __init__(self):
        self._amount = None
        self._arrival_amount = None
        self._bill_cycle = None
        self._bill_desc = None
        self._bill_type = None
        self._billable_type = None
        self._biz_document_no = None
        self._biz_id = None
        self._confirmed_arrival_amount = None
        self._currency = None
        self._deduct_amount = None
        self._detail_ids = None
        self._discharge_amount = None
        self._ext_json = None
        self._gmt_create = None
        self._id = None
        self._invoice_bill_no = None
        self._ou_code = None
        self._pre_invoice_bill_no = None
        self._red = None
        self._related_document_no = None
        self._source_id = None
        self._sync_status = None
        self._tax_rate = None
        self._temp_arrival_amount = None
        self._vendor_id = None
        self._vendor_user_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def arrival_amount(self):
        return self._arrival_amount

    @arrival_amount.setter
    def arrival_amount(self, value):
        self._arrival_amount = value
    @property
    def bill_cycle(self):
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, value):
        self._bill_cycle = value
    @property
    def bill_desc(self):
        return self._bill_desc

    @bill_desc.setter
    def bill_desc(self, value):
        self._bill_desc = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def billable_type(self):
        return self._billable_type

    @billable_type.setter
    def billable_type(self, value):
        self._billable_type = value
    @property
    def biz_document_no(self):
        return self._biz_document_no

    @biz_document_no.setter
    def biz_document_no(self, value):
        self._biz_document_no = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def confirmed_arrival_amount(self):
        return self._confirmed_arrival_amount

    @confirmed_arrival_amount.setter
    def confirmed_arrival_amount(self, value):
        self._confirmed_arrival_amount = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def deduct_amount(self):
        return self._deduct_amount

    @deduct_amount.setter
    def deduct_amount(self, value):
        self._deduct_amount = value
    @property
    def detail_ids(self):
        return self._detail_ids

    @detail_ids.setter
    def detail_ids(self, value):
        if isinstance(value, list):
            self._detail_ids = list()
            for i in value:
                self._detail_ids.append(i)
    @property
    def discharge_amount(self):
        return self._discharge_amount

    @discharge_amount.setter
    def discharge_amount(self, value):
        self._discharge_amount = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def invoice_bill_no(self):
        return self._invoice_bill_no

    @invoice_bill_no.setter
    def invoice_bill_no(self, value):
        self._invoice_bill_no = value
    @property
    def ou_code(self):
        return self._ou_code

    @ou_code.setter
    def ou_code(self, value):
        self._ou_code = value
    @property
    def pre_invoice_bill_no(self):
        return self._pre_invoice_bill_no

    @pre_invoice_bill_no.setter
    def pre_invoice_bill_no(self, value):
        self._pre_invoice_bill_no = value
    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, value):
        self._red = value
    @property
    def related_document_no(self):
        return self._related_document_no

    @related_document_no.setter
    def related_document_no(self, value):
        self._related_document_no = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value
    @property
    def sync_status(self):
        return self._sync_status

    @sync_status.setter
    def sync_status(self, value):
        self._sync_status = value
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def temp_arrival_amount(self):
        return self._temp_arrival_amount

    @temp_arrival_amount.setter
    def temp_arrival_amount(self, value):
        self._temp_arrival_amount = value
    @property
    def vendor_id(self):
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, value):
        self._vendor_id = value
    @property
    def vendor_user_id(self):
        return self._vendor_user_id

    @vendor_user_id.setter
    def vendor_user_id(self, value):
        self._vendor_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.arrival_amount:
            if hasattr(self.arrival_amount, 'to_alipay_dict'):
                params['arrival_amount'] = self.arrival_amount.to_alipay_dict()
            else:
                params['arrival_amount'] = self.arrival_amount
        if self.bill_cycle:
            if hasattr(self.bill_cycle, 'to_alipay_dict'):
                params['bill_cycle'] = self.bill_cycle.to_alipay_dict()
            else:
                params['bill_cycle'] = self.bill_cycle
        if self.bill_desc:
            if hasattr(self.bill_desc, 'to_alipay_dict'):
                params['bill_desc'] = self.bill_desc.to_alipay_dict()
            else:
                params['bill_desc'] = self.bill_desc
        if self.bill_type:
            if hasattr(self.bill_type, 'to_alipay_dict'):
                params['bill_type'] = self.bill_type.to_alipay_dict()
            else:
                params['bill_type'] = self.bill_type
        if self.billable_type:
            if hasattr(self.billable_type, 'to_alipay_dict'):
                params['billable_type'] = self.billable_type.to_alipay_dict()
            else:
                params['billable_type'] = self.billable_type
        if self.biz_document_no:
            if hasattr(self.biz_document_no, 'to_alipay_dict'):
                params['biz_document_no'] = self.biz_document_no.to_alipay_dict()
            else:
                params['biz_document_no'] = self.biz_document_no
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.confirmed_arrival_amount:
            if hasattr(self.confirmed_arrival_amount, 'to_alipay_dict'):
                params['confirmed_arrival_amount'] = self.confirmed_arrival_amount.to_alipay_dict()
            else:
                params['confirmed_arrival_amount'] = self.confirmed_arrival_amount
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.deduct_amount:
            if hasattr(self.deduct_amount, 'to_alipay_dict'):
                params['deduct_amount'] = self.deduct_amount.to_alipay_dict()
            else:
                params['deduct_amount'] = self.deduct_amount
        if self.detail_ids:
            if isinstance(self.detail_ids, list):
                for i in range(0, len(self.detail_ids)):
                    element = self.detail_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detail_ids[i] = element.to_alipay_dict()
            if hasattr(self.detail_ids, 'to_alipay_dict'):
                params['detail_ids'] = self.detail_ids.to_alipay_dict()
            else:
                params['detail_ids'] = self.detail_ids
        if self.discharge_amount:
            if hasattr(self.discharge_amount, 'to_alipay_dict'):
                params['discharge_amount'] = self.discharge_amount.to_alipay_dict()
            else:
                params['discharge_amount'] = self.discharge_amount
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.invoice_bill_no:
            if hasattr(self.invoice_bill_no, 'to_alipay_dict'):
                params['invoice_bill_no'] = self.invoice_bill_no.to_alipay_dict()
            else:
                params['invoice_bill_no'] = self.invoice_bill_no
        if self.ou_code:
            if hasattr(self.ou_code, 'to_alipay_dict'):
                params['ou_code'] = self.ou_code.to_alipay_dict()
            else:
                params['ou_code'] = self.ou_code
        if self.pre_invoice_bill_no:
            if hasattr(self.pre_invoice_bill_no, 'to_alipay_dict'):
                params['pre_invoice_bill_no'] = self.pre_invoice_bill_no.to_alipay_dict()
            else:
                params['pre_invoice_bill_no'] = self.pre_invoice_bill_no
        if self.red:
            if hasattr(self.red, 'to_alipay_dict'):
                params['red'] = self.red.to_alipay_dict()
            else:
                params['red'] = self.red
        if self.related_document_no:
            if hasattr(self.related_document_no, 'to_alipay_dict'):
                params['related_document_no'] = self.related_document_no.to_alipay_dict()
            else:
                params['related_document_no'] = self.related_document_no
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        if self.sync_status:
            if hasattr(self.sync_status, 'to_alipay_dict'):
                params['sync_status'] = self.sync_status.to_alipay_dict()
            else:
                params['sync_status'] = self.sync_status
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.temp_arrival_amount:
            if hasattr(self.temp_arrival_amount, 'to_alipay_dict'):
                params['temp_arrival_amount'] = self.temp_arrival_amount.to_alipay_dict()
            else:
                params['temp_arrival_amount'] = self.temp_arrival_amount
        if self.vendor_id:
            if hasattr(self.vendor_id, 'to_alipay_dict'):
                params['vendor_id'] = self.vendor_id.to_alipay_dict()
            else:
                params['vendor_id'] = self.vendor_id
        if self.vendor_user_id:
            if hasattr(self.vendor_user_id, 'to_alipay_dict'):
                params['vendor_user_id'] = self.vendor_user_id.to_alipay_dict()
            else:
                params['vendor_user_id'] = self.vendor_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceBillDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'arrival_amount' in d:
            o.arrival_amount = d['arrival_amount']
        if 'bill_cycle' in d:
            o.bill_cycle = d['bill_cycle']
        if 'bill_desc' in d:
            o.bill_desc = d['bill_desc']
        if 'bill_type' in d:
            o.bill_type = d['bill_type']
        if 'billable_type' in d:
            o.billable_type = d['billable_type']
        if 'biz_document_no' in d:
            o.biz_document_no = d['biz_document_no']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'confirmed_arrival_amount' in d:
            o.confirmed_arrival_amount = d['confirmed_arrival_amount']
        if 'currency' in d:
            o.currency = d['currency']
        if 'deduct_amount' in d:
            o.deduct_amount = d['deduct_amount']
        if 'detail_ids' in d:
            o.detail_ids = d['detail_ids']
        if 'discharge_amount' in d:
            o.discharge_amount = d['discharge_amount']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'id' in d:
            o.id = d['id']
        if 'invoice_bill_no' in d:
            o.invoice_bill_no = d['invoice_bill_no']
        if 'ou_code' in d:
            o.ou_code = d['ou_code']
        if 'pre_invoice_bill_no' in d:
            o.pre_invoice_bill_no = d['pre_invoice_bill_no']
        if 'red' in d:
            o.red = d['red']
        if 'related_document_no' in d:
            o.related_document_no = d['related_document_no']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'sync_status' in d:
            o.sync_status = d['sync_status']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'temp_arrival_amount' in d:
            o.temp_arrival_amount = d['temp_arrival_amount']
        if 'vendor_id' in d:
            o.vendor_id = d['vendor_id']
        if 'vendor_user_id' in d:
            o.vendor_user_id = d['vendor_user_id']
        return o



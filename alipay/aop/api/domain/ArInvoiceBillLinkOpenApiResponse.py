#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class ArInvoiceBillLinkOpenApiResponse(object):

    def __init__(self):
        self._amt = None
        self._bill_no = None
        self._creator = None
        self._gmt_create = None
        self._gmt_modified = None
        self._inv_rcpt_month = None
        self._invoice_id = None
        self._invoice_receipt_id = None
        self._last_moder = None
        self._link_id = None
        self._out_biz_type = None
        self._ret_amt = None
        self._status = None
        self._tnt_inst_id = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amt = value
        else:
            self._amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
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
    def inv_rcpt_month(self):
        return self._inv_rcpt_month

    @inv_rcpt_month.setter
    def inv_rcpt_month(self, value):
        self._inv_rcpt_month = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def invoice_receipt_id(self):
        return self._invoice_receipt_id

    @invoice_receipt_id.setter
    def invoice_receipt_id(self, value):
        self._invoice_receipt_id = value
    @property
    def last_moder(self):
        return self._last_moder

    @last_moder.setter
    def last_moder(self, value):
        self._last_moder = value
    @property
    def link_id(self):
        return self._link_id

    @link_id.setter
    def link_id(self, value):
        self._link_id = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def ret_amt(self):
        return self._ret_amt

    @ret_amt.setter
    def ret_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._ret_amt = value
        else:
            self._ret_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
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
        if self.inv_rcpt_month:
            if hasattr(self.inv_rcpt_month, 'to_alipay_dict'):
                params['inv_rcpt_month'] = self.inv_rcpt_month.to_alipay_dict()
            else:
                params['inv_rcpt_month'] = self.inv_rcpt_month
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.invoice_receipt_id:
            if hasattr(self.invoice_receipt_id, 'to_alipay_dict'):
                params['invoice_receipt_id'] = self.invoice_receipt_id.to_alipay_dict()
            else:
                params['invoice_receipt_id'] = self.invoice_receipt_id
        if self.last_moder:
            if hasattr(self.last_moder, 'to_alipay_dict'):
                params['last_moder'] = self.last_moder.to_alipay_dict()
            else:
                params['last_moder'] = self.last_moder
        if self.link_id:
            if hasattr(self.link_id, 'to_alipay_dict'):
                params['link_id'] = self.link_id.to_alipay_dict()
            else:
                params['link_id'] = self.link_id
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.ret_amt:
            if hasattr(self.ret_amt, 'to_alipay_dict'):
                params['ret_amt'] = self.ret_amt.to_alipay_dict()
            else:
                params['ret_amt'] = self.ret_amt
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ArInvoiceBillLinkOpenApiResponse()
        if 'amt' in d:
            o.amt = d['amt']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'creator' in d:
            o.creator = d['creator']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'inv_rcpt_month' in d:
            o.inv_rcpt_month = d['inv_rcpt_month']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'invoice_receipt_id' in d:
            o.invoice_receipt_id = d['invoice_receipt_id']
        if 'last_moder' in d:
            o.last_moder = d['last_moder']
        if 'link_id' in d:
            o.link_id = d['link_id']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'ret_amt' in d:
            o.ret_amt = d['ret_amt']
        if 'status' in d:
            o.status = d['status']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o



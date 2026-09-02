#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RemoteExternalBillDetail(object):

    def __init__(self):
        self._bill_date_desc = None
        self._bill_date_end = None
        self._bill_date_start = None
        self._fine_date = None
        self._id = None
        self._memo = None
        self._release_date = None
        self._sequence = None
        self._status = None
        self._total_amount = None

    @property
    def bill_date_desc(self):
        return self._bill_date_desc

    @bill_date_desc.setter
    def bill_date_desc(self, value):
        self._bill_date_desc = value
    @property
    def bill_date_end(self):
        return self._bill_date_end

    @bill_date_end.setter
    def bill_date_end(self, value):
        self._bill_date_end = value
    @property
    def bill_date_start(self):
        return self._bill_date_start

    @bill_date_start.setter
    def bill_date_start(self, value):
        self._bill_date_start = value
    @property
    def fine_date(self):
        return self._fine_date

    @fine_date.setter
    def fine_date(self, value):
        self._fine_date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_date_desc:
            if hasattr(self.bill_date_desc, 'to_alipay_dict'):
                params['bill_date_desc'] = self.bill_date_desc.to_alipay_dict()
            else:
                params['bill_date_desc'] = self.bill_date_desc
        if self.bill_date_end:
            if hasattr(self.bill_date_end, 'to_alipay_dict'):
                params['bill_date_end'] = self.bill_date_end.to_alipay_dict()
            else:
                params['bill_date_end'] = self.bill_date_end
        if self.bill_date_start:
            if hasattr(self.bill_date_start, 'to_alipay_dict'):
                params['bill_date_start'] = self.bill_date_start.to_alipay_dict()
            else:
                params['bill_date_start'] = self.bill_date_start
        if self.fine_date:
            if hasattr(self.fine_date, 'to_alipay_dict'):
                params['fine_date'] = self.fine_date.to_alipay_dict()
            else:
                params['fine_date'] = self.fine_date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.release_date:
            if hasattr(self.release_date, 'to_alipay_dict'):
                params['release_date'] = self.release_date.to_alipay_dict()
            else:
                params['release_date'] = self.release_date
        if self.sequence:
            if hasattr(self.sequence, 'to_alipay_dict'):
                params['sequence'] = self.sequence.to_alipay_dict()
            else:
                params['sequence'] = self.sequence
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = RemoteExternalBillDetail()
        if 'bill_date_desc' in d:
            o.bill_date_desc = d['bill_date_desc']
        if 'bill_date_end' in d:
            o.bill_date_end = d['bill_date_end']
        if 'bill_date_start' in d:
            o.bill_date_start = d['bill_date_start']
        if 'fine_date' in d:
            o.fine_date = d['fine_date']
        if 'id' in d:
            o.id = d['id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'release_date' in d:
            o.release_date = d['release_date']
        if 'sequence' in d:
            o.sequence = d['sequence']
        if 'status' in d:
            o.status = d['status']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



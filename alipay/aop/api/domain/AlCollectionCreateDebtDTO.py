#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollectionFileDTO import CollectionFileDTO


class AlCollectionCreateDebtDTO(object):

    def __init__(self):
        self._files = None
        self._overdue_end_date = None
        self._overdue_start_date = None
        self._overdue_statement = None
        self._total_amount = None

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if isinstance(value, list):
            self._files = list()
            for i in value:
                if isinstance(i, CollectionFileDTO):
                    self._files.append(i)
                else:
                    self._files.append(CollectionFileDTO.from_alipay_dict(i))
    @property
    def overdue_end_date(self):
        return self._overdue_end_date

    @overdue_end_date.setter
    def overdue_end_date(self, value):
        self._overdue_end_date = value
    @property
    def overdue_start_date(self):
        return self._overdue_start_date

    @overdue_start_date.setter
    def overdue_start_date(self, value):
        self._overdue_start_date = value
    @property
    def overdue_statement(self):
        return self._overdue_statement

    @overdue_statement.setter
    def overdue_statement(self, value):
        self._overdue_statement = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.files:
            if isinstance(self.files, list):
                for i in range(0, len(self.files)):
                    element = self.files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.files[i] = element.to_alipay_dict()
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.overdue_end_date:
            if hasattr(self.overdue_end_date, 'to_alipay_dict'):
                params['overdue_end_date'] = self.overdue_end_date.to_alipay_dict()
            else:
                params['overdue_end_date'] = self.overdue_end_date
        if self.overdue_start_date:
            if hasattr(self.overdue_start_date, 'to_alipay_dict'):
                params['overdue_start_date'] = self.overdue_start_date.to_alipay_dict()
            else:
                params['overdue_start_date'] = self.overdue_start_date
        if self.overdue_statement:
            if hasattr(self.overdue_statement, 'to_alipay_dict'):
                params['overdue_statement'] = self.overdue_statement.to_alipay_dict()
            else:
                params['overdue_statement'] = self.overdue_statement
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
        o = AlCollectionCreateDebtDTO()
        if 'files' in d:
            o.files = d['files']
        if 'overdue_end_date' in d:
            o.overdue_end_date = d['overdue_end_date']
        if 'overdue_start_date' in d:
            o.overdue_start_date = d['overdue_start_date']
        if 'overdue_statement' in d:
            o.overdue_statement = d['overdue_statement']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o



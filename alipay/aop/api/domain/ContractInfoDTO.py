#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CollectionFileDTO import CollectionFileDTO
from alipay.aop.api.domain.InvoicingNoAndDate import InvoicingNoAndDate
from alipay.aop.api.domain.CollectionFileDTO import CollectionFileDTO


class ContractInfoDTO(object):

    def __init__(self):
        self._ar_id = None
        self._contract_info_no = None
        self._files = None
        self._invoicing_no_and_date = None
        self._other_files = None

    @property
    def ar_id(self):
        return self._ar_id

    @ar_id.setter
    def ar_id(self, value):
        self._ar_id = value
    @property
    def contract_info_no(self):
        return self._contract_info_no

    @contract_info_no.setter
    def contract_info_no(self, value):
        if isinstance(value, list):
            self._contract_info_no = list()
            for i in value:
                self._contract_info_no.append(i)
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
    def invoicing_no_and_date(self):
        return self._invoicing_no_and_date

    @invoicing_no_and_date.setter
    def invoicing_no_and_date(self, value):
        if isinstance(value, list):
            self._invoicing_no_and_date = list()
            for i in value:
                if isinstance(i, InvoicingNoAndDate):
                    self._invoicing_no_and_date.append(i)
                else:
                    self._invoicing_no_and_date.append(InvoicingNoAndDate.from_alipay_dict(i))
    @property
    def other_files(self):
        return self._other_files

    @other_files.setter
    def other_files(self, value):
        if isinstance(value, list):
            self._other_files = list()
            for i in value:
                if isinstance(i, CollectionFileDTO):
                    self._other_files.append(i)
                else:
                    self._other_files.append(CollectionFileDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.ar_id:
            if hasattr(self.ar_id, 'to_alipay_dict'):
                params['ar_id'] = self.ar_id.to_alipay_dict()
            else:
                params['ar_id'] = self.ar_id
        if self.contract_info_no:
            if isinstance(self.contract_info_no, list):
                for i in range(0, len(self.contract_info_no)):
                    element = self.contract_info_no[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.contract_info_no[i] = element.to_alipay_dict()
            if hasattr(self.contract_info_no, 'to_alipay_dict'):
                params['contract_info_no'] = self.contract_info_no.to_alipay_dict()
            else:
                params['contract_info_no'] = self.contract_info_no
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
        if self.invoicing_no_and_date:
            if isinstance(self.invoicing_no_and_date, list):
                for i in range(0, len(self.invoicing_no_and_date)):
                    element = self.invoicing_no_and_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoicing_no_and_date[i] = element.to_alipay_dict()
            if hasattr(self.invoicing_no_and_date, 'to_alipay_dict'):
                params['invoicing_no_and_date'] = self.invoicing_no_and_date.to_alipay_dict()
            else:
                params['invoicing_no_and_date'] = self.invoicing_no_and_date
        if self.other_files:
            if isinstance(self.other_files, list):
                for i in range(0, len(self.other_files)):
                    element = self.other_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_files[i] = element.to_alipay_dict()
            if hasattr(self.other_files, 'to_alipay_dict'):
                params['other_files'] = self.other_files.to_alipay_dict()
            else:
                params['other_files'] = self.other_files
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractInfoDTO()
        if 'ar_id' in d:
            o.ar_id = d['ar_id']
        if 'contract_info_no' in d:
            o.contract_info_no = d['contract_info_no']
        if 'files' in d:
            o.files = d['files']
        if 'invoicing_no_and_date' in d:
            o.invoicing_no_and_date = d['invoicing_no_and_date']
        if 'other_files' in d:
            o.other_files = d['other_files']
        return o



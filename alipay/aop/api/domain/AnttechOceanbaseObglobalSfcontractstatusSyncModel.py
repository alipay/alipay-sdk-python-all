#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ArchiveFiles import ArchiveFiles


class AnttechOceanbaseObglobalSfcontractstatusSyncModel(object):

    def __init__(self):
        self._archive_files = None
        self._contract_status = None
        self._contract_title = None
        self._contract_view_url = None
        self._customer_contract_fee = None
        self._customer_contract_fee_currency_value = None
        self._effective_date = None
        self._external_contract_id = None
        self._filing_time = None
        self._ob_sign_other_party_subject_name = None
        self._request_id = None

    @property
    def archive_files(self):
        return self._archive_files

    @archive_files.setter
    def archive_files(self, value):
        if isinstance(value, list):
            self._archive_files = list()
            for i in value:
                if isinstance(i, ArchiveFiles):
                    self._archive_files.append(i)
                else:
                    self._archive_files.append(ArchiveFiles.from_alipay_dict(i))
    @property
    def contract_status(self):
        return self._contract_status

    @contract_status.setter
    def contract_status(self, value):
        self._contract_status = value
    @property
    def contract_title(self):
        return self._contract_title

    @contract_title.setter
    def contract_title(self, value):
        self._contract_title = value
    @property
    def contract_view_url(self):
        return self._contract_view_url

    @contract_view_url.setter
    def contract_view_url(self, value):
        self._contract_view_url = value
    @property
    def customer_contract_fee(self):
        return self._customer_contract_fee

    @customer_contract_fee.setter
    def customer_contract_fee(self, value):
        self._customer_contract_fee = value
    @property
    def customer_contract_fee_currency_value(self):
        return self._customer_contract_fee_currency_value

    @customer_contract_fee_currency_value.setter
    def customer_contract_fee_currency_value(self, value):
        self._customer_contract_fee_currency_value = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def external_contract_id(self):
        return self._external_contract_id

    @external_contract_id.setter
    def external_contract_id(self, value):
        self._external_contract_id = value
    @property
    def filing_time(self):
        return self._filing_time

    @filing_time.setter
    def filing_time(self, value):
        self._filing_time = value
    @property
    def ob_sign_other_party_subject_name(self):
        return self._ob_sign_other_party_subject_name

    @ob_sign_other_party_subject_name.setter
    def ob_sign_other_party_subject_name(self, value):
        self._ob_sign_other_party_subject_name = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.archive_files:
            if isinstance(self.archive_files, list):
                for i in range(0, len(self.archive_files)):
                    element = self.archive_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.archive_files[i] = element.to_alipay_dict()
            if hasattr(self.archive_files, 'to_alipay_dict'):
                params['archive_files'] = self.archive_files.to_alipay_dict()
            else:
                params['archive_files'] = self.archive_files
        if self.contract_status:
            if hasattr(self.contract_status, 'to_alipay_dict'):
                params['contract_status'] = self.contract_status.to_alipay_dict()
            else:
                params['contract_status'] = self.contract_status
        if self.contract_title:
            if hasattr(self.contract_title, 'to_alipay_dict'):
                params['contract_title'] = self.contract_title.to_alipay_dict()
            else:
                params['contract_title'] = self.contract_title
        if self.contract_view_url:
            if hasattr(self.contract_view_url, 'to_alipay_dict'):
                params['contract_view_url'] = self.contract_view_url.to_alipay_dict()
            else:
                params['contract_view_url'] = self.contract_view_url
        if self.customer_contract_fee:
            if hasattr(self.customer_contract_fee, 'to_alipay_dict'):
                params['customer_contract_fee'] = self.customer_contract_fee.to_alipay_dict()
            else:
                params['customer_contract_fee'] = self.customer_contract_fee
        if self.customer_contract_fee_currency_value:
            if hasattr(self.customer_contract_fee_currency_value, 'to_alipay_dict'):
                params['customer_contract_fee_currency_value'] = self.customer_contract_fee_currency_value.to_alipay_dict()
            else:
                params['customer_contract_fee_currency_value'] = self.customer_contract_fee_currency_value
        if self.effective_date:
            if hasattr(self.effective_date, 'to_alipay_dict'):
                params['effective_date'] = self.effective_date.to_alipay_dict()
            else:
                params['effective_date'] = self.effective_date
        if self.external_contract_id:
            if hasattr(self.external_contract_id, 'to_alipay_dict'):
                params['external_contract_id'] = self.external_contract_id.to_alipay_dict()
            else:
                params['external_contract_id'] = self.external_contract_id
        if self.filing_time:
            if hasattr(self.filing_time, 'to_alipay_dict'):
                params['filing_time'] = self.filing_time.to_alipay_dict()
            else:
                params['filing_time'] = self.filing_time
        if self.ob_sign_other_party_subject_name:
            if hasattr(self.ob_sign_other_party_subject_name, 'to_alipay_dict'):
                params['ob_sign_other_party_subject_name'] = self.ob_sign_other_party_subject_name.to_alipay_dict()
            else:
                params['ob_sign_other_party_subject_name'] = self.ob_sign_other_party_subject_name
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSfcontractstatusSyncModel()
        if 'archive_files' in d:
            o.archive_files = d['archive_files']
        if 'contract_status' in d:
            o.contract_status = d['contract_status']
        if 'contract_title' in d:
            o.contract_title = d['contract_title']
        if 'contract_view_url' in d:
            o.contract_view_url = d['contract_view_url']
        if 'customer_contract_fee' in d:
            o.customer_contract_fee = d['customer_contract_fee']
        if 'customer_contract_fee_currency_value' in d:
            o.customer_contract_fee_currency_value = d['customer_contract_fee_currency_value']
        if 'effective_date' in d:
            o.effective_date = d['effective_date']
        if 'external_contract_id' in d:
            o.external_contract_id = d['external_contract_id']
        if 'filing_time' in d:
            o.filing_time = d['filing_time']
        if 'ob_sign_other_party_subject_name' in d:
            o.ob_sign_other_party_subject_name = d['ob_sign_other_party_subject_name']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o



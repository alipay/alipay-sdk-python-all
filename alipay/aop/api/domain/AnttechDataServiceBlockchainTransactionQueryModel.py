#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechDataServiceBlockchainTransactionQueryModel(object):

    def __init__(self):
        self._block_chain_id = None
        self._block_hash = None
        self._end_timestamp = None
        self._from_account = None
        self._page_no = None
        self._page_size = None
        self._start_timestamp = None
        self._to_account = None
        self._transaction_hash = None
        self._transaction_type = None

    @property
    def block_chain_id(self):
        return self._block_chain_id

    @block_chain_id.setter
    def block_chain_id(self, value):
        self._block_chain_id = value
    @property
    def block_hash(self):
        return self._block_hash

    @block_hash.setter
    def block_hash(self, value):
        self._block_hash = value
    @property
    def end_timestamp(self):
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, value):
        self._end_timestamp = value
    @property
    def from_account(self):
        return self._from_account

    @from_account.setter
    def from_account(self, value):
        self._from_account = value
    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def start_timestamp(self):
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value):
        self._start_timestamp = value
    @property
    def to_account(self):
        return self._to_account

    @to_account.setter
    def to_account(self, value):
        self._to_account = value
    @property
    def transaction_hash(self):
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, value):
        self._transaction_hash = value
    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.block_chain_id:
            if hasattr(self.block_chain_id, 'to_alipay_dict'):
                params['block_chain_id'] = self.block_chain_id.to_alipay_dict()
            else:
                params['block_chain_id'] = self.block_chain_id
        if self.block_hash:
            if hasattr(self.block_hash, 'to_alipay_dict'):
                params['block_hash'] = self.block_hash.to_alipay_dict()
            else:
                params['block_hash'] = self.block_hash
        if self.end_timestamp:
            if hasattr(self.end_timestamp, 'to_alipay_dict'):
                params['end_timestamp'] = self.end_timestamp.to_alipay_dict()
            else:
                params['end_timestamp'] = self.end_timestamp
        if self.from_account:
            if hasattr(self.from_account, 'to_alipay_dict'):
                params['from_account'] = self.from_account.to_alipay_dict()
            else:
                params['from_account'] = self.from_account
        if self.page_no:
            if hasattr(self.page_no, 'to_alipay_dict'):
                params['page_no'] = self.page_no.to_alipay_dict()
            else:
                params['page_no'] = self.page_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.start_timestamp:
            if hasattr(self.start_timestamp, 'to_alipay_dict'):
                params['start_timestamp'] = self.start_timestamp.to_alipay_dict()
            else:
                params['start_timestamp'] = self.start_timestamp
        if self.to_account:
            if hasattr(self.to_account, 'to_alipay_dict'):
                params['to_account'] = self.to_account.to_alipay_dict()
            else:
                params['to_account'] = self.to_account
        if self.transaction_hash:
            if hasattr(self.transaction_hash, 'to_alipay_dict'):
                params['transaction_hash'] = self.transaction_hash.to_alipay_dict()
            else:
                params['transaction_hash'] = self.transaction_hash
        if self.transaction_type:
            if hasattr(self.transaction_type, 'to_alipay_dict'):
                params['transaction_type'] = self.transaction_type.to_alipay_dict()
            else:
                params['transaction_type'] = self.transaction_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechDataServiceBlockchainTransactionQueryModel()
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'block_hash' in d:
            o.block_hash = d['block_hash']
        if 'end_timestamp' in d:
            o.end_timestamp = d['end_timestamp']
        if 'from_account' in d:
            o.from_account = d['from_account']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_timestamp' in d:
            o.start_timestamp = d['start_timestamp']
        if 'to_account' in d:
            o.to_account = d['to_account']
        if 'transaction_hash' in d:
            o.transaction_hash = d['transaction_hash']
        if 'transaction_type' in d:
            o.transaction_type = d['transaction_type']
        return o



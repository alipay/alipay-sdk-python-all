#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechDataServiceBlockchainContractQueryModel(object):

    def __init__(self):
        self._at_tenant_name = None
        self._block_chain_id = None
        self._block_hash = None
        self._contract_hash = None
        self._end_timestamp = None
        self._page_no = None
        self._page_size = None
        self._start_timestamp = None

    @property
    def at_tenant_name(self):
        return self._at_tenant_name

    @at_tenant_name.setter
    def at_tenant_name(self, value):
        self._at_tenant_name = value
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
    def contract_hash(self):
        return self._contract_hash

    @contract_hash.setter
    def contract_hash(self, value):
        self._contract_hash = value
    @property
    def end_timestamp(self):
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, value):
        self._end_timestamp = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.at_tenant_name:
            if hasattr(self.at_tenant_name, 'to_alipay_dict'):
                params['at_tenant_name'] = self.at_tenant_name.to_alipay_dict()
            else:
                params['at_tenant_name'] = self.at_tenant_name
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
        if self.contract_hash:
            if hasattr(self.contract_hash, 'to_alipay_dict'):
                params['contract_hash'] = self.contract_hash.to_alipay_dict()
            else:
                params['contract_hash'] = self.contract_hash
        if self.end_timestamp:
            if hasattr(self.end_timestamp, 'to_alipay_dict'):
                params['end_timestamp'] = self.end_timestamp.to_alipay_dict()
            else:
                params['end_timestamp'] = self.end_timestamp
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechDataServiceBlockchainContractQueryModel()
        if 'at_tenant_name' in d:
            o.at_tenant_name = d['at_tenant_name']
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'block_hash' in d:
            o.block_hash = d['block_hash']
        if 'contract_hash' in d:
            o.contract_hash = d['contract_hash']
        if 'end_timestamp' in d:
            o.end_timestamp = d['end_timestamp']
        if 'page_no' in d:
            o.page_no = d['page_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'start_timestamp' in d:
            o.start_timestamp = d['start_timestamp']
        return o



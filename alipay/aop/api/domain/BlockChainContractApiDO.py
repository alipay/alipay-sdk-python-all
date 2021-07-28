#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BlockChainContractApiDO(object):

    def __init__(self):
        self._abi = None
        self._block_chain_id = None
        self._block_hash = None
        self._cid = None
        self._code_hash = None
        self._contract_hash = None
        self._contract_timestamp = None
        self._contract_version = None
        self._data = None
        self._ext = None
        self._transaction_hash = None

    @property
    def abi(self):
        return self._abi

    @abi.setter
    def abi(self, value):
        self._abi = value
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
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def code_hash(self):
        return self._code_hash

    @code_hash.setter
    def code_hash(self, value):
        self._code_hash = value
    @property
    def contract_hash(self):
        return self._contract_hash

    @contract_hash.setter
    def contract_hash(self, value):
        self._contract_hash = value
    @property
    def contract_timestamp(self):
        return self._contract_timestamp

    @contract_timestamp.setter
    def contract_timestamp(self, value):
        self._contract_timestamp = value
    @property
    def contract_version(self):
        return self._contract_version

    @contract_version.setter
    def contract_version(self, value):
        self._contract_version = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value
    @property
    def transaction_hash(self):
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, value):
        self._transaction_hash = value


    def to_alipay_dict(self):
        params = dict()
        if self.abi:
            if hasattr(self.abi, 'to_alipay_dict'):
                params['abi'] = self.abi.to_alipay_dict()
            else:
                params['abi'] = self.abi
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
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.code_hash:
            if hasattr(self.code_hash, 'to_alipay_dict'):
                params['code_hash'] = self.code_hash.to_alipay_dict()
            else:
                params['code_hash'] = self.code_hash
        if self.contract_hash:
            if hasattr(self.contract_hash, 'to_alipay_dict'):
                params['contract_hash'] = self.contract_hash.to_alipay_dict()
            else:
                params['contract_hash'] = self.contract_hash
        if self.contract_timestamp:
            if hasattr(self.contract_timestamp, 'to_alipay_dict'):
                params['contract_timestamp'] = self.contract_timestamp.to_alipay_dict()
            else:
                params['contract_timestamp'] = self.contract_timestamp
        if self.contract_version:
            if hasattr(self.contract_version, 'to_alipay_dict'):
                params['contract_version'] = self.contract_version.to_alipay_dict()
            else:
                params['contract_version'] = self.contract_version
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.ext:
            if hasattr(self.ext, 'to_alipay_dict'):
                params['ext'] = self.ext.to_alipay_dict()
            else:
                params['ext'] = self.ext
        if self.transaction_hash:
            if hasattr(self.transaction_hash, 'to_alipay_dict'):
                params['transaction_hash'] = self.transaction_hash.to_alipay_dict()
            else:
                params['transaction_hash'] = self.transaction_hash
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BlockChainContractApiDO()
        if 'abi' in d:
            o.abi = d['abi']
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'block_hash' in d:
            o.block_hash = d['block_hash']
        if 'cid' in d:
            o.cid = d['cid']
        if 'code_hash' in d:
            o.code_hash = d['code_hash']
        if 'contract_hash' in d:
            o.contract_hash = d['contract_hash']
        if 'contract_timestamp' in d:
            o.contract_timestamp = d['contract_timestamp']
        if 'contract_version' in d:
            o.contract_version = d['contract_version']
        if 'data' in d:
            o.data = d['data']
        if 'ext' in d:
            o.ext = d['ext']
        if 'transaction_hash' in d:
            o.transaction_hash = d['transaction_hash']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BlockChainTransactionApiDO(object):

    def __init__(self):
        self._block_chain_id = None
        self._block_hash = None
        self._block_height = None
        self._cid = None
        self._from_account = None
        self._gas_used = None
        self._to_account = None
        self._transaction_hash = None
        self._transaction_timestamp = None
        self._transaction_type = None
        self._value = None

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
    def block_height(self):
        return self._block_height

    @block_height.setter
    def block_height(self, value):
        self._block_height = value
    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        self._cid = value
    @property
    def from_account(self):
        return self._from_account

    @from_account.setter
    def from_account(self, value):
        self._from_account = value
    @property
    def gas_used(self):
        return self._gas_used

    @gas_used.setter
    def gas_used(self, value):
        self._gas_used = value
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
    def transaction_timestamp(self):
        return self._transaction_timestamp

    @transaction_timestamp.setter
    def transaction_timestamp(self, value):
        self._transaction_timestamp = value
    @property
    def transaction_type(self):
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, value):
        self._transaction_type = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


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
        if self.block_height:
            if hasattr(self.block_height, 'to_alipay_dict'):
                params['block_height'] = self.block_height.to_alipay_dict()
            else:
                params['block_height'] = self.block_height
        if self.cid:
            if hasattr(self.cid, 'to_alipay_dict'):
                params['cid'] = self.cid.to_alipay_dict()
            else:
                params['cid'] = self.cid
        if self.from_account:
            if hasattr(self.from_account, 'to_alipay_dict'):
                params['from_account'] = self.from_account.to_alipay_dict()
            else:
                params['from_account'] = self.from_account
        if self.gas_used:
            if hasattr(self.gas_used, 'to_alipay_dict'):
                params['gas_used'] = self.gas_used.to_alipay_dict()
            else:
                params['gas_used'] = self.gas_used
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
        if self.transaction_timestamp:
            if hasattr(self.transaction_timestamp, 'to_alipay_dict'):
                params['transaction_timestamp'] = self.transaction_timestamp.to_alipay_dict()
            else:
                params['transaction_timestamp'] = self.transaction_timestamp
        if self.transaction_type:
            if hasattr(self.transaction_type, 'to_alipay_dict'):
                params['transaction_type'] = self.transaction_type.to_alipay_dict()
            else:
                params['transaction_type'] = self.transaction_type
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BlockChainTransactionApiDO()
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'block_hash' in d:
            o.block_hash = d['block_hash']
        if 'block_height' in d:
            o.block_height = d['block_height']
        if 'cid' in d:
            o.cid = d['cid']
        if 'from_account' in d:
            o.from_account = d['from_account']
        if 'gas_used' in d:
            o.gas_used = d['gas_used']
        if 'to_account' in d:
            o.to_account = d['to_account']
        if 'transaction_hash' in d:
            o.transaction_hash = d['transaction_hash']
        if 'transaction_timestamp' in d:
            o.transaction_timestamp = d['transaction_timestamp']
        if 'transaction_type' in d:
            o.transaction_type = d['transaction_type']
        if 'value' in d:
            o.value = d['value']
        return o



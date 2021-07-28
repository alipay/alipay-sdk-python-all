#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BlockChainAccountApiDO(object):

    def __init__(self):
        self._account_hash = None
        self._account_index = None
        self._account_name = None
        self._account_status = None
        self._balance = None
        self._block_chain_id = None
        self._block_hash = None
        self._cid = None
        self._create_time = None
        self._parent_hash = None
        self._transaction_hash = None

    @property
    def account_hash(self):
        return self._account_hash

    @account_hash.setter
    def account_hash(self, value):
        self._account_hash = value
    @property
    def account_index(self):
        return self._account_index

    @account_index.setter
    def account_index(self, value):
        self._account_index = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, value):
        self._account_status = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def parent_hash(self):
        return self._parent_hash

    @parent_hash.setter
    def parent_hash(self, value):
        self._parent_hash = value
    @property
    def transaction_hash(self):
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, value):
        self._transaction_hash = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_hash:
            if hasattr(self.account_hash, 'to_alipay_dict'):
                params['account_hash'] = self.account_hash.to_alipay_dict()
            else:
                params['account_hash'] = self.account_hash
        if self.account_index:
            if hasattr(self.account_index, 'to_alipay_dict'):
                params['account_index'] = self.account_index.to_alipay_dict()
            else:
                params['account_index'] = self.account_index
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_status:
            if hasattr(self.account_status, 'to_alipay_dict'):
                params['account_status'] = self.account_status.to_alipay_dict()
            else:
                params['account_status'] = self.account_status
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
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
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.parent_hash:
            if hasattr(self.parent_hash, 'to_alipay_dict'):
                params['parent_hash'] = self.parent_hash.to_alipay_dict()
            else:
                params['parent_hash'] = self.parent_hash
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
        o = BlockChainAccountApiDO()
        if 'account_hash' in d:
            o.account_hash = d['account_hash']
        if 'account_index' in d:
            o.account_index = d['account_index']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_status' in d:
            o.account_status = d['account_status']
        if 'balance' in d:
            o.balance = d['balance']
        if 'block_chain_id' in d:
            o.block_chain_id = d['block_chain_id']
        if 'block_hash' in d:
            o.block_hash = d['block_hash']
        if 'cid' in d:
            o.cid = d['cid']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'parent_hash' in d:
            o.parent_hash = d['parent_hash']
        if 'transaction_hash' in d:
            o.transaction_hash = d['transaction_hash']
        return o



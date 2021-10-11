#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class CollectReceiptOpenApiDTO(object):

    def __init__(self):
        self._bsn_no = None
        self._bsn_ref_no = None
        self._business_scene = None
        self._channel = None
        self._channel_log_no = None
        self._channel_memo = None
        self._collect_amt = None
        self._collect_date = None
        self._collect_status = None
        self._collected_amt = None
        self._creator = None
        self._freeze_amt = None
        self._fund_log_id = None
        self._gl_exchange_rate = None
        self._gmt_create = None
        self._gmt_modified = None
        self._payee_account_name = None
        self._payee_account_no = None
        self._payee_inst_id = None
        self._payee_ip_role_id = None
        self._payer_account_name = None
        self._payer_account_no = None
        self._payer_bank_branch_name = None
        self._payer_inst_id = None
        self._payer_ip_role_id = None
        self._receipt_no = None
        self._ref_trans_no = None
        self._ref_trans_no_type = None
        self._source = None
        self._status = None
        self._tnt_inst_id = None
        self._used_amt = None
        self._writeoff_relative_id = None

    @property
    def bsn_no(self):
        return self._bsn_no

    @bsn_no.setter
    def bsn_no(self, value):
        self._bsn_no = value
    @property
    def bsn_ref_no(self):
        return self._bsn_ref_no

    @bsn_ref_no.setter
    def bsn_ref_no(self, value):
        self._bsn_ref_no = value
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_log_no(self):
        return self._channel_log_no

    @channel_log_no.setter
    def channel_log_no(self, value):
        self._channel_log_no = value
    @property
    def channel_memo(self):
        return self._channel_memo

    @channel_memo.setter
    def channel_memo(self, value):
        self._channel_memo = value
    @property
    def collect_amt(self):
        return self._collect_amt

    @collect_amt.setter
    def collect_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._collect_amt = value
        else:
            self._collect_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def collect_date(self):
        return self._collect_date

    @collect_date.setter
    def collect_date(self, value):
        self._collect_date = value
    @property
    def collect_status(self):
        return self._collect_status

    @collect_status.setter
    def collect_status(self, value):
        self._collect_status = value
    @property
    def collected_amt(self):
        return self._collected_amt

    @collected_amt.setter
    def collected_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._collected_amt = value
        else:
            self._collected_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def freeze_amt(self):
        return self._freeze_amt

    @freeze_amt.setter
    def freeze_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._freeze_amt = value
        else:
            self._freeze_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def fund_log_id(self):
        return self._fund_log_id

    @fund_log_id.setter
    def fund_log_id(self, value):
        self._fund_log_id = value
    @property
    def gl_exchange_rate(self):
        return self._gl_exchange_rate

    @gl_exchange_rate.setter
    def gl_exchange_rate(self, value):
        self._gl_exchange_rate = value
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
    def payee_account_name(self):
        return self._payee_account_name

    @payee_account_name.setter
    def payee_account_name(self, value):
        self._payee_account_name = value
    @property
    def payee_account_no(self):
        return self._payee_account_no

    @payee_account_no.setter
    def payee_account_no(self, value):
        self._payee_account_no = value
    @property
    def payee_inst_id(self):
        return self._payee_inst_id

    @payee_inst_id.setter
    def payee_inst_id(self, value):
        self._payee_inst_id = value
    @property
    def payee_ip_role_id(self):
        return self._payee_ip_role_id

    @payee_ip_role_id.setter
    def payee_ip_role_id(self, value):
        self._payee_ip_role_id = value
    @property
    def payer_account_name(self):
        return self._payer_account_name

    @payer_account_name.setter
    def payer_account_name(self, value):
        self._payer_account_name = value
    @property
    def payer_account_no(self):
        return self._payer_account_no

    @payer_account_no.setter
    def payer_account_no(self, value):
        self._payer_account_no = value
    @property
    def payer_bank_branch_name(self):
        return self._payer_bank_branch_name

    @payer_bank_branch_name.setter
    def payer_bank_branch_name(self, value):
        self._payer_bank_branch_name = value
    @property
    def payer_inst_id(self):
        return self._payer_inst_id

    @payer_inst_id.setter
    def payer_inst_id(self, value):
        self._payer_inst_id = value
    @property
    def payer_ip_role_id(self):
        return self._payer_ip_role_id

    @payer_ip_role_id.setter
    def payer_ip_role_id(self, value):
        self._payer_ip_role_id = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def ref_trans_no(self):
        return self._ref_trans_no

    @ref_trans_no.setter
    def ref_trans_no(self, value):
        self._ref_trans_no = value
    @property
    def ref_trans_no_type(self):
        return self._ref_trans_no_type

    @ref_trans_no_type.setter
    def ref_trans_no_type(self, value):
        self._ref_trans_no_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
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
    @property
    def used_amt(self):
        return self._used_amt

    @used_amt.setter
    def used_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._used_amt = value
        else:
            self._used_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def writeoff_relative_id(self):
        return self._writeoff_relative_id

    @writeoff_relative_id.setter
    def writeoff_relative_id(self, value):
        self._writeoff_relative_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bsn_no:
            if hasattr(self.bsn_no, 'to_alipay_dict'):
                params['bsn_no'] = self.bsn_no.to_alipay_dict()
            else:
                params['bsn_no'] = self.bsn_no
        if self.bsn_ref_no:
            if hasattr(self.bsn_ref_no, 'to_alipay_dict'):
                params['bsn_ref_no'] = self.bsn_ref_no.to_alipay_dict()
            else:
                params['bsn_ref_no'] = self.bsn_ref_no
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_log_no:
            if hasattr(self.channel_log_no, 'to_alipay_dict'):
                params['channel_log_no'] = self.channel_log_no.to_alipay_dict()
            else:
                params['channel_log_no'] = self.channel_log_no
        if self.channel_memo:
            if hasattr(self.channel_memo, 'to_alipay_dict'):
                params['channel_memo'] = self.channel_memo.to_alipay_dict()
            else:
                params['channel_memo'] = self.channel_memo
        if self.collect_amt:
            if hasattr(self.collect_amt, 'to_alipay_dict'):
                params['collect_amt'] = self.collect_amt.to_alipay_dict()
            else:
                params['collect_amt'] = self.collect_amt
        if self.collect_date:
            if hasattr(self.collect_date, 'to_alipay_dict'):
                params['collect_date'] = self.collect_date.to_alipay_dict()
            else:
                params['collect_date'] = self.collect_date
        if self.collect_status:
            if hasattr(self.collect_status, 'to_alipay_dict'):
                params['collect_status'] = self.collect_status.to_alipay_dict()
            else:
                params['collect_status'] = self.collect_status
        if self.collected_amt:
            if hasattr(self.collected_amt, 'to_alipay_dict'):
                params['collected_amt'] = self.collected_amt.to_alipay_dict()
            else:
                params['collected_amt'] = self.collected_amt
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.freeze_amt:
            if hasattr(self.freeze_amt, 'to_alipay_dict'):
                params['freeze_amt'] = self.freeze_amt.to_alipay_dict()
            else:
                params['freeze_amt'] = self.freeze_amt
        if self.fund_log_id:
            if hasattr(self.fund_log_id, 'to_alipay_dict'):
                params['fund_log_id'] = self.fund_log_id.to_alipay_dict()
            else:
                params['fund_log_id'] = self.fund_log_id
        if self.gl_exchange_rate:
            if hasattr(self.gl_exchange_rate, 'to_alipay_dict'):
                params['gl_exchange_rate'] = self.gl_exchange_rate.to_alipay_dict()
            else:
                params['gl_exchange_rate'] = self.gl_exchange_rate
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
        if self.payee_account_name:
            if hasattr(self.payee_account_name, 'to_alipay_dict'):
                params['payee_account_name'] = self.payee_account_name.to_alipay_dict()
            else:
                params['payee_account_name'] = self.payee_account_name
        if self.payee_account_no:
            if hasattr(self.payee_account_no, 'to_alipay_dict'):
                params['payee_account_no'] = self.payee_account_no.to_alipay_dict()
            else:
                params['payee_account_no'] = self.payee_account_no
        if self.payee_inst_id:
            if hasattr(self.payee_inst_id, 'to_alipay_dict'):
                params['payee_inst_id'] = self.payee_inst_id.to_alipay_dict()
            else:
                params['payee_inst_id'] = self.payee_inst_id
        if self.payee_ip_role_id:
            if hasattr(self.payee_ip_role_id, 'to_alipay_dict'):
                params['payee_ip_role_id'] = self.payee_ip_role_id.to_alipay_dict()
            else:
                params['payee_ip_role_id'] = self.payee_ip_role_id
        if self.payer_account_name:
            if hasattr(self.payer_account_name, 'to_alipay_dict'):
                params['payer_account_name'] = self.payer_account_name.to_alipay_dict()
            else:
                params['payer_account_name'] = self.payer_account_name
        if self.payer_account_no:
            if hasattr(self.payer_account_no, 'to_alipay_dict'):
                params['payer_account_no'] = self.payer_account_no.to_alipay_dict()
            else:
                params['payer_account_no'] = self.payer_account_no
        if self.payer_bank_branch_name:
            if hasattr(self.payer_bank_branch_name, 'to_alipay_dict'):
                params['payer_bank_branch_name'] = self.payer_bank_branch_name.to_alipay_dict()
            else:
                params['payer_bank_branch_name'] = self.payer_bank_branch_name
        if self.payer_inst_id:
            if hasattr(self.payer_inst_id, 'to_alipay_dict'):
                params['payer_inst_id'] = self.payer_inst_id.to_alipay_dict()
            else:
                params['payer_inst_id'] = self.payer_inst_id
        if self.payer_ip_role_id:
            if hasattr(self.payer_ip_role_id, 'to_alipay_dict'):
                params['payer_ip_role_id'] = self.payer_ip_role_id.to_alipay_dict()
            else:
                params['payer_ip_role_id'] = self.payer_ip_role_id
        if self.receipt_no:
            if hasattr(self.receipt_no, 'to_alipay_dict'):
                params['receipt_no'] = self.receipt_no.to_alipay_dict()
            else:
                params['receipt_no'] = self.receipt_no
        if self.ref_trans_no:
            if hasattr(self.ref_trans_no, 'to_alipay_dict'):
                params['ref_trans_no'] = self.ref_trans_no.to_alipay_dict()
            else:
                params['ref_trans_no'] = self.ref_trans_no
        if self.ref_trans_no_type:
            if hasattr(self.ref_trans_no_type, 'to_alipay_dict'):
                params['ref_trans_no_type'] = self.ref_trans_no_type.to_alipay_dict()
            else:
                params['ref_trans_no_type'] = self.ref_trans_no_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        if self.used_amt:
            if hasattr(self.used_amt, 'to_alipay_dict'):
                params['used_amt'] = self.used_amt.to_alipay_dict()
            else:
                params['used_amt'] = self.used_amt
        if self.writeoff_relative_id:
            if hasattr(self.writeoff_relative_id, 'to_alipay_dict'):
                params['writeoff_relative_id'] = self.writeoff_relative_id.to_alipay_dict()
            else:
                params['writeoff_relative_id'] = self.writeoff_relative_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectReceiptOpenApiDTO()
        if 'bsn_no' in d:
            o.bsn_no = d['bsn_no']
        if 'bsn_ref_no' in d:
            o.bsn_ref_no = d['bsn_ref_no']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_log_no' in d:
            o.channel_log_no = d['channel_log_no']
        if 'channel_memo' in d:
            o.channel_memo = d['channel_memo']
        if 'collect_amt' in d:
            o.collect_amt = d['collect_amt']
        if 'collect_date' in d:
            o.collect_date = d['collect_date']
        if 'collect_status' in d:
            o.collect_status = d['collect_status']
        if 'collected_amt' in d:
            o.collected_amt = d['collected_amt']
        if 'creator' in d:
            o.creator = d['creator']
        if 'freeze_amt' in d:
            o.freeze_amt = d['freeze_amt']
        if 'fund_log_id' in d:
            o.fund_log_id = d['fund_log_id']
        if 'gl_exchange_rate' in d:
            o.gl_exchange_rate = d['gl_exchange_rate']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'payee_account_name' in d:
            o.payee_account_name = d['payee_account_name']
        if 'payee_account_no' in d:
            o.payee_account_no = d['payee_account_no']
        if 'payee_inst_id' in d:
            o.payee_inst_id = d['payee_inst_id']
        if 'payee_ip_role_id' in d:
            o.payee_ip_role_id = d['payee_ip_role_id']
        if 'payer_account_name' in d:
            o.payer_account_name = d['payer_account_name']
        if 'payer_account_no' in d:
            o.payer_account_no = d['payer_account_no']
        if 'payer_bank_branch_name' in d:
            o.payer_bank_branch_name = d['payer_bank_branch_name']
        if 'payer_inst_id' in d:
            o.payer_inst_id = d['payer_inst_id']
        if 'payer_ip_role_id' in d:
            o.payer_ip_role_id = d['payer_ip_role_id']
        if 'receipt_no' in d:
            o.receipt_no = d['receipt_no']
        if 'ref_trans_no' in d:
            o.ref_trans_no = d['ref_trans_no']
        if 'ref_trans_no_type' in d:
            o.ref_trans_no_type = d['ref_trans_no_type']
        if 'source' in d:
            o.source = d['source']
        if 'status' in d:
            o.status = d['status']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'used_amt' in d:
            o.used_amt = d['used_amt']
        if 'writeoff_relative_id' in d:
            o.writeoff_relative_id = d['writeoff_relative_id']
        return o



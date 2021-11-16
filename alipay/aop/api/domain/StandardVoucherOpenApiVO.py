#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.AccountInfoVO import AccountInfoVO
from alipay.aop.api.domain.AccountInfoVO import AccountInfoVO
from alipay.aop.api.domain.AccountInfoVO import AccountInfoVO
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class StandardVoucherOpenApiVO(object):

    def __init__(self):
        self._algorithm_tag = None
        self._balance = None
        self._charge_amount = None
        self._coa_properties = None
        self._dt = None
        self._dw_log_type = None
        self._event_code = None
        self._ext_info = None
        self._fund_biz_code = None
        self._fund_biz_name = None
        self._gmt_create = None
        self._gmt_modified = None
        self._handle_status = None
        self._hour = None
        self._id = None
        self._idempotent_id = None
        self._inst_serial_no = None
        self._manual_dist_demo = None
        self._manual_dist_type = None
        self._memo = None
        self._operator = None
        self._org_trans_no = None
        self._ori_trans_amount = None
        self._ori_trans_rate = None
        self._other_account = None
        self._out_biz_no = None
        self._prod_code = None
        self._rel_voucher_id = None
        self._status = None
        self._target_account = None
        self._tnt_inst_id = None
        self._trans_account = None
        self._trans_amount = None
        self._trans_direction = None
        self._trans_dt = None
        self._trans_inst_id = None
        self._tx_id = None
        self._voucher_type = None
        self._writeoff_voucher_id = None

    @property
    def algorithm_tag(self):
        return self._algorithm_tag

    @algorithm_tag.setter
    def algorithm_tag(self, value):
        self._algorithm_tag = value
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._balance = value
        else:
            self._balance = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def charge_amount(self):
        return self._charge_amount

    @charge_amount.setter
    def charge_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._charge_amount = value
        else:
            self._charge_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def coa_properties(self):
        return self._coa_properties

    @coa_properties.setter
    def coa_properties(self, value):
        self._coa_properties = value
    @property
    def dt(self):
        return self._dt

    @dt.setter
    def dt(self, value):
        self._dt = value
    @property
    def dw_log_type(self):
        return self._dw_log_type

    @dw_log_type.setter
    def dw_log_type(self, value):
        self._dw_log_type = value
    @property
    def event_code(self):
        return self._event_code

    @event_code.setter
    def event_code(self, value):
        self._event_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def fund_biz_code(self):
        return self._fund_biz_code

    @fund_biz_code.setter
    def fund_biz_code(self, value):
        self._fund_biz_code = value
    @property
    def fund_biz_name(self):
        return self._fund_biz_name

    @fund_biz_name.setter
    def fund_biz_name(self, value):
        self._fund_biz_name = value
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
    def handle_status(self):
        return self._handle_status

    @handle_status.setter
    def handle_status(self, value):
        self._handle_status = value
    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        self._hour = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def idempotent_id(self):
        return self._idempotent_id

    @idempotent_id.setter
    def idempotent_id(self, value):
        self._idempotent_id = value
    @property
    def inst_serial_no(self):
        return self._inst_serial_no

    @inst_serial_no.setter
    def inst_serial_no(self, value):
        self._inst_serial_no = value
    @property
    def manual_dist_demo(self):
        return self._manual_dist_demo

    @manual_dist_demo.setter
    def manual_dist_demo(self, value):
        self._manual_dist_demo = value
    @property
    def manual_dist_type(self):
        return self._manual_dist_type

    @manual_dist_type.setter
    def manual_dist_type(self, value):
        self._manual_dist_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def org_trans_no(self):
        return self._org_trans_no

    @org_trans_no.setter
    def org_trans_no(self, value):
        self._org_trans_no = value
    @property
    def ori_trans_amount(self):
        return self._ori_trans_amount

    @ori_trans_amount.setter
    def ori_trans_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._ori_trans_amount = value
        else:
            self._ori_trans_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def ori_trans_rate(self):
        return self._ori_trans_rate

    @ori_trans_rate.setter
    def ori_trans_rate(self, value):
        self._ori_trans_rate = value
    @property
    def other_account(self):
        return self._other_account

    @other_account.setter
    def other_account(self, value):
        if isinstance(value, AccountInfoVO):
            self._other_account = value
        else:
            self._other_account = AccountInfoVO.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def rel_voucher_id(self):
        return self._rel_voucher_id

    @rel_voucher_id.setter
    def rel_voucher_id(self, value):
        self._rel_voucher_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def target_account(self):
        return self._target_account

    @target_account.setter
    def target_account(self, value):
        if isinstance(value, AccountInfoVO):
            self._target_account = value
        else:
            self._target_account = AccountInfoVO.from_alipay_dict(value)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def trans_account(self):
        return self._trans_account

    @trans_account.setter
    def trans_account(self, value):
        if isinstance(value, AccountInfoVO):
            self._trans_account = value
        else:
            self._trans_account = AccountInfoVO.from_alipay_dict(value)
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._trans_amount = value
        else:
            self._trans_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def trans_direction(self):
        return self._trans_direction

    @trans_direction.setter
    def trans_direction(self, value):
        self._trans_direction = value
    @property
    def trans_dt(self):
        return self._trans_dt

    @trans_dt.setter
    def trans_dt(self, value):
        self._trans_dt = value
    @property
    def trans_inst_id(self):
        return self._trans_inst_id

    @trans_inst_id.setter
    def trans_inst_id(self, value):
        self._trans_inst_id = value
    @property
    def tx_id(self):
        return self._tx_id

    @tx_id.setter
    def tx_id(self, value):
        self._tx_id = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value
    @property
    def writeoff_voucher_id(self):
        return self._writeoff_voucher_id

    @writeoff_voucher_id.setter
    def writeoff_voucher_id(self, value):
        self._writeoff_voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_tag:
            if hasattr(self.algorithm_tag, 'to_alipay_dict'):
                params['algorithm_tag'] = self.algorithm_tag.to_alipay_dict()
            else:
                params['algorithm_tag'] = self.algorithm_tag
        if self.balance:
            if hasattr(self.balance, 'to_alipay_dict'):
                params['balance'] = self.balance.to_alipay_dict()
            else:
                params['balance'] = self.balance
        if self.charge_amount:
            if hasattr(self.charge_amount, 'to_alipay_dict'):
                params['charge_amount'] = self.charge_amount.to_alipay_dict()
            else:
                params['charge_amount'] = self.charge_amount
        if self.coa_properties:
            if hasattr(self.coa_properties, 'to_alipay_dict'):
                params['coa_properties'] = self.coa_properties.to_alipay_dict()
            else:
                params['coa_properties'] = self.coa_properties
        if self.dt:
            if hasattr(self.dt, 'to_alipay_dict'):
                params['dt'] = self.dt.to_alipay_dict()
            else:
                params['dt'] = self.dt
        if self.dw_log_type:
            if hasattr(self.dw_log_type, 'to_alipay_dict'):
                params['dw_log_type'] = self.dw_log_type.to_alipay_dict()
            else:
                params['dw_log_type'] = self.dw_log_type
        if self.event_code:
            if hasattr(self.event_code, 'to_alipay_dict'):
                params['event_code'] = self.event_code.to_alipay_dict()
            else:
                params['event_code'] = self.event_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.fund_biz_code:
            if hasattr(self.fund_biz_code, 'to_alipay_dict'):
                params['fund_biz_code'] = self.fund_biz_code.to_alipay_dict()
            else:
                params['fund_biz_code'] = self.fund_biz_code
        if self.fund_biz_name:
            if hasattr(self.fund_biz_name, 'to_alipay_dict'):
                params['fund_biz_name'] = self.fund_biz_name.to_alipay_dict()
            else:
                params['fund_biz_name'] = self.fund_biz_name
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
        if self.handle_status:
            if hasattr(self.handle_status, 'to_alipay_dict'):
                params['handle_status'] = self.handle_status.to_alipay_dict()
            else:
                params['handle_status'] = self.handle_status
        if self.hour:
            if hasattr(self.hour, 'to_alipay_dict'):
                params['hour'] = self.hour.to_alipay_dict()
            else:
                params['hour'] = self.hour
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.idempotent_id:
            if hasattr(self.idempotent_id, 'to_alipay_dict'):
                params['idempotent_id'] = self.idempotent_id.to_alipay_dict()
            else:
                params['idempotent_id'] = self.idempotent_id
        if self.inst_serial_no:
            if hasattr(self.inst_serial_no, 'to_alipay_dict'):
                params['inst_serial_no'] = self.inst_serial_no.to_alipay_dict()
            else:
                params['inst_serial_no'] = self.inst_serial_no
        if self.manual_dist_demo:
            if hasattr(self.manual_dist_demo, 'to_alipay_dict'):
                params['manual_dist_demo'] = self.manual_dist_demo.to_alipay_dict()
            else:
                params['manual_dist_demo'] = self.manual_dist_demo
        if self.manual_dist_type:
            if hasattr(self.manual_dist_type, 'to_alipay_dict'):
                params['manual_dist_type'] = self.manual_dist_type.to_alipay_dict()
            else:
                params['manual_dist_type'] = self.manual_dist_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.org_trans_no:
            if hasattr(self.org_trans_no, 'to_alipay_dict'):
                params['org_trans_no'] = self.org_trans_no.to_alipay_dict()
            else:
                params['org_trans_no'] = self.org_trans_no
        if self.ori_trans_amount:
            if hasattr(self.ori_trans_amount, 'to_alipay_dict'):
                params['ori_trans_amount'] = self.ori_trans_amount.to_alipay_dict()
            else:
                params['ori_trans_amount'] = self.ori_trans_amount
        if self.ori_trans_rate:
            if hasattr(self.ori_trans_rate, 'to_alipay_dict'):
                params['ori_trans_rate'] = self.ori_trans_rate.to_alipay_dict()
            else:
                params['ori_trans_rate'] = self.ori_trans_rate
        if self.other_account:
            if hasattr(self.other_account, 'to_alipay_dict'):
                params['other_account'] = self.other_account.to_alipay_dict()
            else:
                params['other_account'] = self.other_account
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.rel_voucher_id:
            if hasattr(self.rel_voucher_id, 'to_alipay_dict'):
                params['rel_voucher_id'] = self.rel_voucher_id.to_alipay_dict()
            else:
                params['rel_voucher_id'] = self.rel_voucher_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.target_account:
            if hasattr(self.target_account, 'to_alipay_dict'):
                params['target_account'] = self.target_account.to_alipay_dict()
            else:
                params['target_account'] = self.target_account
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.trans_account:
            if hasattr(self.trans_account, 'to_alipay_dict'):
                params['trans_account'] = self.trans_account.to_alipay_dict()
            else:
                params['trans_account'] = self.trans_account
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_direction:
            if hasattr(self.trans_direction, 'to_alipay_dict'):
                params['trans_direction'] = self.trans_direction.to_alipay_dict()
            else:
                params['trans_direction'] = self.trans_direction
        if self.trans_dt:
            if hasattr(self.trans_dt, 'to_alipay_dict'):
                params['trans_dt'] = self.trans_dt.to_alipay_dict()
            else:
                params['trans_dt'] = self.trans_dt
        if self.trans_inst_id:
            if hasattr(self.trans_inst_id, 'to_alipay_dict'):
                params['trans_inst_id'] = self.trans_inst_id.to_alipay_dict()
            else:
                params['trans_inst_id'] = self.trans_inst_id
        if self.tx_id:
            if hasattr(self.tx_id, 'to_alipay_dict'):
                params['tx_id'] = self.tx_id.to_alipay_dict()
            else:
                params['tx_id'] = self.tx_id
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        if self.writeoff_voucher_id:
            if hasattr(self.writeoff_voucher_id, 'to_alipay_dict'):
                params['writeoff_voucher_id'] = self.writeoff_voucher_id.to_alipay_dict()
            else:
                params['writeoff_voucher_id'] = self.writeoff_voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardVoucherOpenApiVO()
        if 'algorithm_tag' in d:
            o.algorithm_tag = d['algorithm_tag']
        if 'balance' in d:
            o.balance = d['balance']
        if 'charge_amount' in d:
            o.charge_amount = d['charge_amount']
        if 'coa_properties' in d:
            o.coa_properties = d['coa_properties']
        if 'dt' in d:
            o.dt = d['dt']
        if 'dw_log_type' in d:
            o.dw_log_type = d['dw_log_type']
        if 'event_code' in d:
            o.event_code = d['event_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'fund_biz_code' in d:
            o.fund_biz_code = d['fund_biz_code']
        if 'fund_biz_name' in d:
            o.fund_biz_name = d['fund_biz_name']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'handle_status' in d:
            o.handle_status = d['handle_status']
        if 'hour' in d:
            o.hour = d['hour']
        if 'id' in d:
            o.id = d['id']
        if 'idempotent_id' in d:
            o.idempotent_id = d['idempotent_id']
        if 'inst_serial_no' in d:
            o.inst_serial_no = d['inst_serial_no']
        if 'manual_dist_demo' in d:
            o.manual_dist_demo = d['manual_dist_demo']
        if 'manual_dist_type' in d:
            o.manual_dist_type = d['manual_dist_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'org_trans_no' in d:
            o.org_trans_no = d['org_trans_no']
        if 'ori_trans_amount' in d:
            o.ori_trans_amount = d['ori_trans_amount']
        if 'ori_trans_rate' in d:
            o.ori_trans_rate = d['ori_trans_rate']
        if 'other_account' in d:
            o.other_account = d['other_account']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'rel_voucher_id' in d:
            o.rel_voucher_id = d['rel_voucher_id']
        if 'status' in d:
            o.status = d['status']
        if 'target_account' in d:
            o.target_account = d['target_account']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'trans_account' in d:
            o.trans_account = d['trans_account']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_direction' in d:
            o.trans_direction = d['trans_direction']
        if 'trans_dt' in d:
            o.trans_dt = d['trans_dt']
        if 'trans_inst_id' in d:
            o.trans_inst_id = d['trans_inst_id']
        if 'tx_id' in d:
            o.tx_id = d['tx_id']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        if 'writeoff_voucher_id' in d:
            o.writeoff_voucher_id = d['writeoff_voucher_id']
        return o



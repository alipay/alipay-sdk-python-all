#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MyBkAccountVO import MyBkAccountVO


class MybankCreditLoantradeLoanarCreateModel(object):

    def __init__(self):
        self._account_ext_no = None
        self._account_fin_code = None
        self._account_fin_name = None
        self._account_fin_type = None
        self._account_name = None
        self._account_no = None
        self._account_type = None
        self._alipay_id = None
        self._apply_amt = None
        self._bsn_no = None
        self._bsn_type = None
        self._credit_no = None
        self._cust_group = None
        self._grant_channel = None
        self._industry = None
        self._ip_id = None
        self._ip_role_id = None
        self._loan_policy_code = None
        self._loan_term = None
        self._loan_term_unit = None
        self._need_check_account_same_name = None
        self._need_sign_contract = None
        self._pd_code = None
        self._pd_version = None
        self._promo_tools = None
        self._repay_account = None
        self._repay_mode = None
        self._request_id = None
        self._sign = None
        self._trans_memo = None

    @property
    def account_ext_no(self):
        return self._account_ext_no

    @account_ext_no.setter
    def account_ext_no(self, value):
        self._account_ext_no = value
    @property
    def account_fin_code(self):
        return self._account_fin_code

    @account_fin_code.setter
    def account_fin_code(self, value):
        self._account_fin_code = value
    @property
    def account_fin_name(self):
        return self._account_fin_name

    @account_fin_name.setter
    def account_fin_name(self, value):
        self._account_fin_name = value
    @property
    def account_fin_type(self):
        return self._account_fin_type

    @account_fin_type.setter
    def account_fin_type(self, value):
        self._account_fin_type = value
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        self._account_name = value
    @property
    def account_no(self):
        return self._account_no

    @account_no.setter
    def account_no(self, value):
        self._account_no = value
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        self._account_type = value
    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def bsn_no(self):
        return self._bsn_no

    @bsn_no.setter
    def bsn_no(self, value):
        self._bsn_no = value
    @property
    def bsn_type(self):
        return self._bsn_type

    @bsn_type.setter
    def bsn_type(self, value):
        self._bsn_type = value
    @property
    def credit_no(self):
        return self._credit_no

    @credit_no.setter
    def credit_no(self, value):
        self._credit_no = value
    @property
    def cust_group(self):
        return self._cust_group

    @cust_group.setter
    def cust_group(self, value):
        self._cust_group = value
    @property
    def grant_channel(self):
        return self._grant_channel

    @grant_channel.setter
    def grant_channel(self, value):
        self._grant_channel = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_policy_code(self):
        return self._loan_policy_code

    @loan_policy_code.setter
    def loan_policy_code(self, value):
        self._loan_policy_code = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def need_check_account_same_name(self):
        return self._need_check_account_same_name

    @need_check_account_same_name.setter
    def need_check_account_same_name(self, value):
        self._need_check_account_same_name = value
    @property
    def need_sign_contract(self):
        return self._need_sign_contract

    @need_sign_contract.setter
    def need_sign_contract(self, value):
        self._need_sign_contract = value
    @property
    def pd_code(self):
        return self._pd_code

    @pd_code.setter
    def pd_code(self, value):
        self._pd_code = value
    @property
    def pd_version(self):
        return self._pd_version

    @pd_version.setter
    def pd_version(self, value):
        self._pd_version = value
    @property
    def promo_tools(self):
        return self._promo_tools

    @promo_tools.setter
    def promo_tools(self, value):
        if isinstance(value, list):
            self._promo_tools = list()
            for i in value:
                self._promo_tools.append(i)
    @property
    def repay_account(self):
        return self._repay_account

    @repay_account.setter
    def repay_account(self, value):
        if isinstance(value, MyBkAccountVO):
            self._repay_account = value
        else:
            self._repay_account = MyBkAccountVO.from_alipay_dict(value)
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, value):
        self._sign = value
    @property
    def trans_memo(self):
        return self._trans_memo

    @trans_memo.setter
    def trans_memo(self, value):
        self._trans_memo = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_ext_no:
            if hasattr(self.account_ext_no, 'to_alipay_dict'):
                params['account_ext_no'] = self.account_ext_no.to_alipay_dict()
            else:
                params['account_ext_no'] = self.account_ext_no
        if self.account_fin_code:
            if hasattr(self.account_fin_code, 'to_alipay_dict'):
                params['account_fin_code'] = self.account_fin_code.to_alipay_dict()
            else:
                params['account_fin_code'] = self.account_fin_code
        if self.account_fin_name:
            if hasattr(self.account_fin_name, 'to_alipay_dict'):
                params['account_fin_name'] = self.account_fin_name.to_alipay_dict()
            else:
                params['account_fin_name'] = self.account_fin_name
        if self.account_fin_type:
            if hasattr(self.account_fin_type, 'to_alipay_dict'):
                params['account_fin_type'] = self.account_fin_type.to_alipay_dict()
            else:
                params['account_fin_type'] = self.account_fin_type
        if self.account_name:
            if hasattr(self.account_name, 'to_alipay_dict'):
                params['account_name'] = self.account_name.to_alipay_dict()
            else:
                params['account_name'] = self.account_name
        if self.account_no:
            if hasattr(self.account_no, 'to_alipay_dict'):
                params['account_no'] = self.account_no.to_alipay_dict()
            else:
                params['account_no'] = self.account_no
        if self.account_type:
            if hasattr(self.account_type, 'to_alipay_dict'):
                params['account_type'] = self.account_type.to_alipay_dict()
            else:
                params['account_type'] = self.account_type
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.bsn_no:
            if hasattr(self.bsn_no, 'to_alipay_dict'):
                params['bsn_no'] = self.bsn_no.to_alipay_dict()
            else:
                params['bsn_no'] = self.bsn_no
        if self.bsn_type:
            if hasattr(self.bsn_type, 'to_alipay_dict'):
                params['bsn_type'] = self.bsn_type.to_alipay_dict()
            else:
                params['bsn_type'] = self.bsn_type
        if self.credit_no:
            if hasattr(self.credit_no, 'to_alipay_dict'):
                params['credit_no'] = self.credit_no.to_alipay_dict()
            else:
                params['credit_no'] = self.credit_no
        if self.cust_group:
            if hasattr(self.cust_group, 'to_alipay_dict'):
                params['cust_group'] = self.cust_group.to_alipay_dict()
            else:
                params['cust_group'] = self.cust_group
        if self.grant_channel:
            if hasattr(self.grant_channel, 'to_alipay_dict'):
                params['grant_channel'] = self.grant_channel.to_alipay_dict()
            else:
                params['grant_channel'] = self.grant_channel
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.loan_policy_code:
            if hasattr(self.loan_policy_code, 'to_alipay_dict'):
                params['loan_policy_code'] = self.loan_policy_code.to_alipay_dict()
            else:
                params['loan_policy_code'] = self.loan_policy_code
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.loan_term_unit:
            if hasattr(self.loan_term_unit, 'to_alipay_dict'):
                params['loan_term_unit'] = self.loan_term_unit.to_alipay_dict()
            else:
                params['loan_term_unit'] = self.loan_term_unit
        if self.need_check_account_same_name:
            if hasattr(self.need_check_account_same_name, 'to_alipay_dict'):
                params['need_check_account_same_name'] = self.need_check_account_same_name.to_alipay_dict()
            else:
                params['need_check_account_same_name'] = self.need_check_account_same_name
        if self.need_sign_contract:
            if hasattr(self.need_sign_contract, 'to_alipay_dict'):
                params['need_sign_contract'] = self.need_sign_contract.to_alipay_dict()
            else:
                params['need_sign_contract'] = self.need_sign_contract
        if self.pd_code:
            if hasattr(self.pd_code, 'to_alipay_dict'):
                params['pd_code'] = self.pd_code.to_alipay_dict()
            else:
                params['pd_code'] = self.pd_code
        if self.pd_version:
            if hasattr(self.pd_version, 'to_alipay_dict'):
                params['pd_version'] = self.pd_version.to_alipay_dict()
            else:
                params['pd_version'] = self.pd_version
        if self.promo_tools:
            if isinstance(self.promo_tools, list):
                for i in range(0, len(self.promo_tools)):
                    element = self.promo_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.promo_tools[i] = element.to_alipay_dict()
            if hasattr(self.promo_tools, 'to_alipay_dict'):
                params['promo_tools'] = self.promo_tools.to_alipay_dict()
            else:
                params['promo_tools'] = self.promo_tools
        if self.repay_account:
            if hasattr(self.repay_account, 'to_alipay_dict'):
                params['repay_account'] = self.repay_account.to_alipay_dict()
            else:
                params['repay_account'] = self.repay_account
        if self.repay_mode:
            if hasattr(self.repay_mode, 'to_alipay_dict'):
                params['repay_mode'] = self.repay_mode.to_alipay_dict()
            else:
                params['repay_mode'] = self.repay_mode
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sign:
            if hasattr(self.sign, 'to_alipay_dict'):
                params['sign'] = self.sign.to_alipay_dict()
            else:
                params['sign'] = self.sign
        if self.trans_memo:
            if hasattr(self.trans_memo, 'to_alipay_dict'):
                params['trans_memo'] = self.trans_memo.to_alipay_dict()
            else:
                params['trans_memo'] = self.trans_memo
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeLoanarCreateModel()
        if 'account_ext_no' in d:
            o.account_ext_no = d['account_ext_no']
        if 'account_fin_code' in d:
            o.account_fin_code = d['account_fin_code']
        if 'account_fin_name' in d:
            o.account_fin_name = d['account_fin_name']
        if 'account_fin_type' in d:
            o.account_fin_type = d['account_fin_type']
        if 'account_name' in d:
            o.account_name = d['account_name']
        if 'account_no' in d:
            o.account_no = d['account_no']
        if 'account_type' in d:
            o.account_type = d['account_type']
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'bsn_no' in d:
            o.bsn_no = d['bsn_no']
        if 'bsn_type' in d:
            o.bsn_type = d['bsn_type']
        if 'credit_no' in d:
            o.credit_no = d['credit_no']
        if 'cust_group' in d:
            o.cust_group = d['cust_group']
        if 'grant_channel' in d:
            o.grant_channel = d['grant_channel']
        if 'industry' in d:
            o.industry = d['industry']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'loan_policy_code' in d:
            o.loan_policy_code = d['loan_policy_code']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'loan_term_unit' in d:
            o.loan_term_unit = d['loan_term_unit']
        if 'need_check_account_same_name' in d:
            o.need_check_account_same_name = d['need_check_account_same_name']
        if 'need_sign_contract' in d:
            o.need_sign_contract = d['need_sign_contract']
        if 'pd_code' in d:
            o.pd_code = d['pd_code']
        if 'pd_version' in d:
            o.pd_version = d['pd_version']
        if 'promo_tools' in d:
            o.promo_tools = d['promo_tools']
        if 'repay_account' in d:
            o.repay_account = d['repay_account']
        if 'repay_mode' in d:
            o.repay_mode = d['repay_mode']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sign' in d:
            o.sign = d['sign']
        if 'trans_memo' in d:
            o.trans_memo = d['trans_memo']
        return o



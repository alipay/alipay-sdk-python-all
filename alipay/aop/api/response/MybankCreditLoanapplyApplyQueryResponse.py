#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ApproveCreditResult import ApproveCreditResult
from alipay.aop.api.domain.InvestigCategoryResult import InvestigCategoryResult


class MybankCreditLoanapplyApplyQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyApplyQueryResponse, self).__init__()
        self._apply_amt = None
        self._apply_date = None
        self._apply_no = None
        self._apply_status = None
        self._approve_conclu = None
        self._approve_credit_result = None
        self._approve_finish_date = None
        self._cust_inst_appid = None
        self._cust_inst_code = None
        self._ext_json = None
        self._investig_category_result = None
        self._ip_role_id = None
        self._loan_type = None
        self._op_prod_code = None
        self._op_prod_code_version = None
        self._refuse_code = None
        self._result = None
        self._state = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def approve_conclu(self):
        return self._approve_conclu

    @approve_conclu.setter
    def approve_conclu(self, value):
        self._approve_conclu = value
    @property
    def approve_credit_result(self):
        return self._approve_credit_result

    @approve_credit_result.setter
    def approve_credit_result(self, value):
        if isinstance(value, ApproveCreditResult):
            self._approve_credit_result = value
        else:
            self._approve_credit_result = ApproveCreditResult.from_alipay_dict(value)
    @property
    def approve_finish_date(self):
        return self._approve_finish_date

    @approve_finish_date.setter
    def approve_finish_date(self, value):
        self._approve_finish_date = value
    @property
    def cust_inst_appid(self):
        return self._cust_inst_appid

    @cust_inst_appid.setter
    def cust_inst_appid(self, value):
        self._cust_inst_appid = value
    @property
    def cust_inst_code(self):
        return self._cust_inst_code

    @cust_inst_code.setter
    def cust_inst_code(self, value):
        self._cust_inst_code = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def investig_category_result(self):
        return self._investig_category_result

    @investig_category_result.setter
    def investig_category_result(self, value):
        if isinstance(value, list):
            self._investig_category_result = list()
            for i in value:
                if isinstance(i, InvestigCategoryResult):
                    self._investig_category_result.append(i)
                else:
                    self._investig_category_result.append(InvestigCategoryResult.from_alipay_dict(i))
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def loan_type(self):
        return self._loan_type

    @loan_type.setter
    def loan_type(self, value):
        self._loan_type = value
    @property
    def op_prod_code(self):
        return self._op_prod_code

    @op_prod_code.setter
    def op_prod_code(self, value):
        self._op_prod_code = value
    @property
    def op_prod_code_version(self):
        return self._op_prod_code_version

    @op_prod_code_version.setter
    def op_prod_code_version(self, value):
        self._op_prod_code_version = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyApplyQueryResponse, self).parse_response_content(response_content)
        if 'apply_amt' in response:
            self.apply_amt = response['apply_amt']
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'apply_status' in response:
            self.apply_status = response['apply_status']
        if 'approve_conclu' in response:
            self.approve_conclu = response['approve_conclu']
        if 'approve_credit_result' in response:
            self.approve_credit_result = response['approve_credit_result']
        if 'approve_finish_date' in response:
            self.approve_finish_date = response['approve_finish_date']
        if 'cust_inst_appid' in response:
            self.cust_inst_appid = response['cust_inst_appid']
        if 'cust_inst_code' in response:
            self.cust_inst_code = response['cust_inst_code']
        if 'ext_json' in response:
            self.ext_json = response['ext_json']
        if 'investig_category_result' in response:
            self.investig_category_result = response['investig_category_result']
        if 'ip_role_id' in response:
            self.ip_role_id = response['ip_role_id']
        if 'loan_type' in response:
            self.loan_type = response['loan_type']
        if 'op_prod_code' in response:
            self.op_prod_code = response['op_prod_code']
        if 'op_prod_code_version' in response:
            self.op_prod_code_version = response['op_prod_code_version']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'result' in response:
            self.result = response['result']
        if 'state' in response:
            self.state = response['state']

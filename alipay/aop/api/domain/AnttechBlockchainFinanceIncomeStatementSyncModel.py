#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StatementDetaileds import StatementDetaileds


class AnttechBlockchainFinanceIncomeStatementSyncModel(object):

    def __init__(self):
        self._biz_no = None
        self._deduction_amount = None
        self._detailed_summary_amount = None
        self._distribution_pro_no = None
        self._distribution_rule_id = None
        self._receivable_amount = None
        self._statement_detaileds = None
        self._statement_file_id = None
        self._statement_issue_date = None
        self._statement_no = None
        self._statistics_end_date = None
        self._statistics_start_date = None
        self._supplementary_amount = None
        self._trade_id = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def detailed_summary_amount(self):
        return self._detailed_summary_amount

    @detailed_summary_amount.setter
    def detailed_summary_amount(self, value):
        self._detailed_summary_amount = value
    @property
    def distribution_pro_no(self):
        return self._distribution_pro_no

    @distribution_pro_no.setter
    def distribution_pro_no(self, value):
        self._distribution_pro_no = value
    @property
    def distribution_rule_id(self):
        return self._distribution_rule_id

    @distribution_rule_id.setter
    def distribution_rule_id(self, value):
        self._distribution_rule_id = value
    @property
    def receivable_amount(self):
        return self._receivable_amount

    @receivable_amount.setter
    def receivable_amount(self, value):
        self._receivable_amount = value
    @property
    def statement_detaileds(self):
        return self._statement_detaileds

    @statement_detaileds.setter
    def statement_detaileds(self, value):
        if isinstance(value, StatementDetaileds):
            self._statement_detaileds = value
        else:
            self._statement_detaileds = StatementDetaileds.from_alipay_dict(value)
    @property
    def statement_file_id(self):
        return self._statement_file_id

    @statement_file_id.setter
    def statement_file_id(self, value):
        self._statement_file_id = value
    @property
    def statement_issue_date(self):
        return self._statement_issue_date

    @statement_issue_date.setter
    def statement_issue_date(self, value):
        self._statement_issue_date = value
    @property
    def statement_no(self):
        return self._statement_no

    @statement_no.setter
    def statement_no(self, value):
        self._statement_no = value
    @property
    def statistics_end_date(self):
        return self._statistics_end_date

    @statistics_end_date.setter
    def statistics_end_date(self, value):
        self._statistics_end_date = value
    @property
    def statistics_start_date(self):
        return self._statistics_start_date

    @statistics_start_date.setter
    def statistics_start_date(self, value):
        self._statistics_start_date = value
    @property
    def supplementary_amount(self):
        return self._supplementary_amount

    @supplementary_amount.setter
    def supplementary_amount(self, value):
        self._supplementary_amount = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.detailed_summary_amount:
            if hasattr(self.detailed_summary_amount, 'to_alipay_dict'):
                params['detailed_summary_amount'] = self.detailed_summary_amount.to_alipay_dict()
            else:
                params['detailed_summary_amount'] = self.detailed_summary_amount
        if self.distribution_pro_no:
            if hasattr(self.distribution_pro_no, 'to_alipay_dict'):
                params['distribution_pro_no'] = self.distribution_pro_no.to_alipay_dict()
            else:
                params['distribution_pro_no'] = self.distribution_pro_no
        if self.distribution_rule_id:
            if hasattr(self.distribution_rule_id, 'to_alipay_dict'):
                params['distribution_rule_id'] = self.distribution_rule_id.to_alipay_dict()
            else:
                params['distribution_rule_id'] = self.distribution_rule_id
        if self.receivable_amount:
            if hasattr(self.receivable_amount, 'to_alipay_dict'):
                params['receivable_amount'] = self.receivable_amount.to_alipay_dict()
            else:
                params['receivable_amount'] = self.receivable_amount
        if self.statement_detaileds:
            if hasattr(self.statement_detaileds, 'to_alipay_dict'):
                params['statement_detaileds'] = self.statement_detaileds.to_alipay_dict()
            else:
                params['statement_detaileds'] = self.statement_detaileds
        if self.statement_file_id:
            if hasattr(self.statement_file_id, 'to_alipay_dict'):
                params['statement_file_id'] = self.statement_file_id.to_alipay_dict()
            else:
                params['statement_file_id'] = self.statement_file_id
        if self.statement_issue_date:
            if hasattr(self.statement_issue_date, 'to_alipay_dict'):
                params['statement_issue_date'] = self.statement_issue_date.to_alipay_dict()
            else:
                params['statement_issue_date'] = self.statement_issue_date
        if self.statement_no:
            if hasattr(self.statement_no, 'to_alipay_dict'):
                params['statement_no'] = self.statement_no.to_alipay_dict()
            else:
                params['statement_no'] = self.statement_no
        if self.statistics_end_date:
            if hasattr(self.statistics_end_date, 'to_alipay_dict'):
                params['statistics_end_date'] = self.statistics_end_date.to_alipay_dict()
            else:
                params['statistics_end_date'] = self.statistics_end_date
        if self.statistics_start_date:
            if hasattr(self.statistics_start_date, 'to_alipay_dict'):
                params['statistics_start_date'] = self.statistics_start_date.to_alipay_dict()
            else:
                params['statistics_start_date'] = self.statistics_start_date
        if self.supplementary_amount:
            if hasattr(self.supplementary_amount, 'to_alipay_dict'):
                params['supplementary_amount'] = self.supplementary_amount.to_alipay_dict()
            else:
                params['supplementary_amount'] = self.supplementary_amount
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceIncomeStatementSyncModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'detailed_summary_amount' in d:
            o.detailed_summary_amount = d['detailed_summary_amount']
        if 'distribution_pro_no' in d:
            o.distribution_pro_no = d['distribution_pro_no']
        if 'distribution_rule_id' in d:
            o.distribution_rule_id = d['distribution_rule_id']
        if 'receivable_amount' in d:
            o.receivable_amount = d['receivable_amount']
        if 'statement_detaileds' in d:
            o.statement_detaileds = d['statement_detaileds']
        if 'statement_file_id' in d:
            o.statement_file_id = d['statement_file_id']
        if 'statement_issue_date' in d:
            o.statement_issue_date = d['statement_issue_date']
        if 'statement_no' in d:
            o.statement_no = d['statement_no']
        if 'statistics_end_date' in d:
            o.statistics_end_date = d['statistics_end_date']
        if 'statistics_start_date' in d:
            o.statistics_start_date = d['statistics_start_date']
        if 'supplementary_amount' in d:
            o.supplementary_amount = d['supplementary_amount']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o



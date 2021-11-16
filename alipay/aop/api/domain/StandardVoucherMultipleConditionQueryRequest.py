#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoney import MultiCurrencyMoney


class StandardVoucherMultipleConditionQueryRequest(object):

    def __init__(self):
        self._account_alias_name = None
        self._account_no_list = None
        self._algorithm_tag = None
        self._black_trans_account_no_list = None
        self._black_trans_inst_id_list = None
        self._cur_page = None
        self._env = None
        self._fund_biz_code_list = None
        self._handle_status_list = None
        self._inst_serial_no = None
        self._manual_dist_memo = None
        self._manual_dist_type_list = None
        self._memo = None
        self._org_trans_no = None
        self._other_account_alias_name = None
        self._other_account_name = None
        self._other_account_no = None
        self._page_size = None
        self._query_source = None
        self._sort_type = None
        self._status_list = None
        self._tnt_inst_id = None
        self._trans_amount = None
        self._trans_currency = None
        self._trans_direction_list = None
        self._trans_end = None
        self._trans_inst_id_list = None
        self._trans_start = None
        self._voucher_type = None

    @property
    def account_alias_name(self):
        return self._account_alias_name

    @account_alias_name.setter
    def account_alias_name(self, value):
        self._account_alias_name = value
    @property
    def account_no_list(self):
        return self._account_no_list

    @account_no_list.setter
    def account_no_list(self, value):
        if isinstance(value, list):
            self._account_no_list = list()
            for i in value:
                self._account_no_list.append(i)
    @property
    def algorithm_tag(self):
        return self._algorithm_tag

    @algorithm_tag.setter
    def algorithm_tag(self, value):
        self._algorithm_tag = value
    @property
    def black_trans_account_no_list(self):
        return self._black_trans_account_no_list

    @black_trans_account_no_list.setter
    def black_trans_account_no_list(self, value):
        if isinstance(value, list):
            self._black_trans_account_no_list = list()
            for i in value:
                self._black_trans_account_no_list.append(i)
    @property
    def black_trans_inst_id_list(self):
        return self._black_trans_inst_id_list

    @black_trans_inst_id_list.setter
    def black_trans_inst_id_list(self, value):
        if isinstance(value, list):
            self._black_trans_inst_id_list = list()
            for i in value:
                self._black_trans_inst_id_list.append(i)
    @property
    def cur_page(self):
        return self._cur_page

    @cur_page.setter
    def cur_page(self, value):
        self._cur_page = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def fund_biz_code_list(self):
        return self._fund_biz_code_list

    @fund_biz_code_list.setter
    def fund_biz_code_list(self, value):
        if isinstance(value, list):
            self._fund_biz_code_list = list()
            for i in value:
                self._fund_biz_code_list.append(i)
    @property
    def handle_status_list(self):
        return self._handle_status_list

    @handle_status_list.setter
    def handle_status_list(self, value):
        if isinstance(value, list):
            self._handle_status_list = list()
            for i in value:
                self._handle_status_list.append(i)
    @property
    def inst_serial_no(self):
        return self._inst_serial_no

    @inst_serial_no.setter
    def inst_serial_no(self, value):
        self._inst_serial_no = value
    @property
    def manual_dist_memo(self):
        return self._manual_dist_memo

    @manual_dist_memo.setter
    def manual_dist_memo(self, value):
        self._manual_dist_memo = value
    @property
    def manual_dist_type_list(self):
        return self._manual_dist_type_list

    @manual_dist_type_list.setter
    def manual_dist_type_list(self, value):
        if isinstance(value, list):
            self._manual_dist_type_list = list()
            for i in value:
                self._manual_dist_type_list.append(i)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def org_trans_no(self):
        return self._org_trans_no

    @org_trans_no.setter
    def org_trans_no(self, value):
        self._org_trans_no = value
    @property
    def other_account_alias_name(self):
        return self._other_account_alias_name

    @other_account_alias_name.setter
    def other_account_alias_name(self, value):
        self._other_account_alias_name = value
    @property
    def other_account_name(self):
        return self._other_account_name

    @other_account_name.setter
    def other_account_name(self, value):
        self._other_account_name = value
    @property
    def other_account_no(self):
        return self._other_account_no

    @other_account_no.setter
    def other_account_no(self, value):
        self._other_account_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def query_source(self):
        return self._query_source

    @query_source.setter
    def query_source(self, value):
        self._query_source = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def status_list(self):
        return self._status_list

    @status_list.setter
    def status_list(self, value):
        if isinstance(value, list):
            self._status_list = list()
            for i in value:
                self._status_list.append(i)
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def trans_amount(self):
        return self._trans_amount

    @trans_amount.setter
    def trans_amount(self, value):
        if isinstance(value, MultiCurrencyMoney):
            self._trans_amount = value
        else:
            self._trans_amount = MultiCurrencyMoney.from_alipay_dict(value)
    @property
    def trans_currency(self):
        return self._trans_currency

    @trans_currency.setter
    def trans_currency(self, value):
        self._trans_currency = value
    @property
    def trans_direction_list(self):
        return self._trans_direction_list

    @trans_direction_list.setter
    def trans_direction_list(self, value):
        if isinstance(value, list):
            self._trans_direction_list = list()
            for i in value:
                self._trans_direction_list.append(i)
    @property
    def trans_end(self):
        return self._trans_end

    @trans_end.setter
    def trans_end(self, value):
        self._trans_end = value
    @property
    def trans_inst_id_list(self):
        return self._trans_inst_id_list

    @trans_inst_id_list.setter
    def trans_inst_id_list(self, value):
        if isinstance(value, list):
            self._trans_inst_id_list = list()
            for i in value:
                self._trans_inst_id_list.append(i)
    @property
    def trans_start(self):
        return self._trans_start

    @trans_start.setter
    def trans_start(self, value):
        self._trans_start = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_alias_name:
            if hasattr(self.account_alias_name, 'to_alipay_dict'):
                params['account_alias_name'] = self.account_alias_name.to_alipay_dict()
            else:
                params['account_alias_name'] = self.account_alias_name
        if self.account_no_list:
            if isinstance(self.account_no_list, list):
                for i in range(0, len(self.account_no_list)):
                    element = self.account_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.account_no_list[i] = element.to_alipay_dict()
            if hasattr(self.account_no_list, 'to_alipay_dict'):
                params['account_no_list'] = self.account_no_list.to_alipay_dict()
            else:
                params['account_no_list'] = self.account_no_list
        if self.algorithm_tag:
            if hasattr(self.algorithm_tag, 'to_alipay_dict'):
                params['algorithm_tag'] = self.algorithm_tag.to_alipay_dict()
            else:
                params['algorithm_tag'] = self.algorithm_tag
        if self.black_trans_account_no_list:
            if isinstance(self.black_trans_account_no_list, list):
                for i in range(0, len(self.black_trans_account_no_list)):
                    element = self.black_trans_account_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.black_trans_account_no_list[i] = element.to_alipay_dict()
            if hasattr(self.black_trans_account_no_list, 'to_alipay_dict'):
                params['black_trans_account_no_list'] = self.black_trans_account_no_list.to_alipay_dict()
            else:
                params['black_trans_account_no_list'] = self.black_trans_account_no_list
        if self.black_trans_inst_id_list:
            if isinstance(self.black_trans_inst_id_list, list):
                for i in range(0, len(self.black_trans_inst_id_list)):
                    element = self.black_trans_inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.black_trans_inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.black_trans_inst_id_list, 'to_alipay_dict'):
                params['black_trans_inst_id_list'] = self.black_trans_inst_id_list.to_alipay_dict()
            else:
                params['black_trans_inst_id_list'] = self.black_trans_inst_id_list
        if self.cur_page:
            if hasattr(self.cur_page, 'to_alipay_dict'):
                params['cur_page'] = self.cur_page.to_alipay_dict()
            else:
                params['cur_page'] = self.cur_page
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.fund_biz_code_list:
            if isinstance(self.fund_biz_code_list, list):
                for i in range(0, len(self.fund_biz_code_list)):
                    element = self.fund_biz_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_biz_code_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_biz_code_list, 'to_alipay_dict'):
                params['fund_biz_code_list'] = self.fund_biz_code_list.to_alipay_dict()
            else:
                params['fund_biz_code_list'] = self.fund_biz_code_list
        if self.handle_status_list:
            if isinstance(self.handle_status_list, list):
                for i in range(0, len(self.handle_status_list)):
                    element = self.handle_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.handle_status_list[i] = element.to_alipay_dict()
            if hasattr(self.handle_status_list, 'to_alipay_dict'):
                params['handle_status_list'] = self.handle_status_list.to_alipay_dict()
            else:
                params['handle_status_list'] = self.handle_status_list
        if self.inst_serial_no:
            if hasattr(self.inst_serial_no, 'to_alipay_dict'):
                params['inst_serial_no'] = self.inst_serial_no.to_alipay_dict()
            else:
                params['inst_serial_no'] = self.inst_serial_no
        if self.manual_dist_memo:
            if hasattr(self.manual_dist_memo, 'to_alipay_dict'):
                params['manual_dist_memo'] = self.manual_dist_memo.to_alipay_dict()
            else:
                params['manual_dist_memo'] = self.manual_dist_memo
        if self.manual_dist_type_list:
            if isinstance(self.manual_dist_type_list, list):
                for i in range(0, len(self.manual_dist_type_list)):
                    element = self.manual_dist_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.manual_dist_type_list[i] = element.to_alipay_dict()
            if hasattr(self.manual_dist_type_list, 'to_alipay_dict'):
                params['manual_dist_type_list'] = self.manual_dist_type_list.to_alipay_dict()
            else:
                params['manual_dist_type_list'] = self.manual_dist_type_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.org_trans_no:
            if hasattr(self.org_trans_no, 'to_alipay_dict'):
                params['org_trans_no'] = self.org_trans_no.to_alipay_dict()
            else:
                params['org_trans_no'] = self.org_trans_no
        if self.other_account_alias_name:
            if hasattr(self.other_account_alias_name, 'to_alipay_dict'):
                params['other_account_alias_name'] = self.other_account_alias_name.to_alipay_dict()
            else:
                params['other_account_alias_name'] = self.other_account_alias_name
        if self.other_account_name:
            if hasattr(self.other_account_name, 'to_alipay_dict'):
                params['other_account_name'] = self.other_account_name.to_alipay_dict()
            else:
                params['other_account_name'] = self.other_account_name
        if self.other_account_no:
            if hasattr(self.other_account_no, 'to_alipay_dict'):
                params['other_account_no'] = self.other_account_no.to_alipay_dict()
            else:
                params['other_account_no'] = self.other_account_no
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.query_source:
            if hasattr(self.query_source, 'to_alipay_dict'):
                params['query_source'] = self.query_source.to_alipay_dict()
            else:
                params['query_source'] = self.query_source
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.status_list:
            if isinstance(self.status_list, list):
                for i in range(0, len(self.status_list)):
                    element = self.status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status_list[i] = element.to_alipay_dict()
            if hasattr(self.status_list, 'to_alipay_dict'):
                params['status_list'] = self.status_list.to_alipay_dict()
            else:
                params['status_list'] = self.status_list
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.trans_amount:
            if hasattr(self.trans_amount, 'to_alipay_dict'):
                params['trans_amount'] = self.trans_amount.to_alipay_dict()
            else:
                params['trans_amount'] = self.trans_amount
        if self.trans_currency:
            if hasattr(self.trans_currency, 'to_alipay_dict'):
                params['trans_currency'] = self.trans_currency.to_alipay_dict()
            else:
                params['trans_currency'] = self.trans_currency
        if self.trans_direction_list:
            if isinstance(self.trans_direction_list, list):
                for i in range(0, len(self.trans_direction_list)):
                    element = self.trans_direction_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_direction_list[i] = element.to_alipay_dict()
            if hasattr(self.trans_direction_list, 'to_alipay_dict'):
                params['trans_direction_list'] = self.trans_direction_list.to_alipay_dict()
            else:
                params['trans_direction_list'] = self.trans_direction_list
        if self.trans_end:
            if hasattr(self.trans_end, 'to_alipay_dict'):
                params['trans_end'] = self.trans_end.to_alipay_dict()
            else:
                params['trans_end'] = self.trans_end
        if self.trans_inst_id_list:
            if isinstance(self.trans_inst_id_list, list):
                for i in range(0, len(self.trans_inst_id_list)):
                    element = self.trans_inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trans_inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.trans_inst_id_list, 'to_alipay_dict'):
                params['trans_inst_id_list'] = self.trans_inst_id_list.to_alipay_dict()
            else:
                params['trans_inst_id_list'] = self.trans_inst_id_list
        if self.trans_start:
            if hasattr(self.trans_start, 'to_alipay_dict'):
                params['trans_start'] = self.trans_start.to_alipay_dict()
            else:
                params['trans_start'] = self.trans_start
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StandardVoucherMultipleConditionQueryRequest()
        if 'account_alias_name' in d:
            o.account_alias_name = d['account_alias_name']
        if 'account_no_list' in d:
            o.account_no_list = d['account_no_list']
        if 'algorithm_tag' in d:
            o.algorithm_tag = d['algorithm_tag']
        if 'black_trans_account_no_list' in d:
            o.black_trans_account_no_list = d['black_trans_account_no_list']
        if 'black_trans_inst_id_list' in d:
            o.black_trans_inst_id_list = d['black_trans_inst_id_list']
        if 'cur_page' in d:
            o.cur_page = d['cur_page']
        if 'env' in d:
            o.env = d['env']
        if 'fund_biz_code_list' in d:
            o.fund_biz_code_list = d['fund_biz_code_list']
        if 'handle_status_list' in d:
            o.handle_status_list = d['handle_status_list']
        if 'inst_serial_no' in d:
            o.inst_serial_no = d['inst_serial_no']
        if 'manual_dist_memo' in d:
            o.manual_dist_memo = d['manual_dist_memo']
        if 'manual_dist_type_list' in d:
            o.manual_dist_type_list = d['manual_dist_type_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'org_trans_no' in d:
            o.org_trans_no = d['org_trans_no']
        if 'other_account_alias_name' in d:
            o.other_account_alias_name = d['other_account_alias_name']
        if 'other_account_name' in d:
            o.other_account_name = d['other_account_name']
        if 'other_account_no' in d:
            o.other_account_no = d['other_account_no']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'query_source' in d:
            o.query_source = d['query_source']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'status_list' in d:
            o.status_list = d['status_list']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'trans_amount' in d:
            o.trans_amount = d['trans_amount']
        if 'trans_currency' in d:
            o.trans_currency = d['trans_currency']
        if 'trans_direction_list' in d:
            o.trans_direction_list = d['trans_direction_list']
        if 'trans_end' in d:
            o.trans_end = d['trans_end']
        if 'trans_inst_id_list' in d:
            o.trans_inst_id_list = d['trans_inst_id_list']
        if 'trans_start' in d:
            o.trans_start = d['trans_start']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o



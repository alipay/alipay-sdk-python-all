#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseDocsyncBanklogQueryModel(object):

    def __init__(self):
        self._current_page = None
        self._dist_memo = None
        self._dist_type_list = None
        self._drct_list = None
        self._erecon_biz_type_code = None
        self._fin_biz_code_list = None
        self._fundlog_source = None
        self._inner_account_no = None
        self._inst_id_list = None
        self._inst_serial_no = None
        self._log_status = None
        self._memo = None
        self._other_account_name = None
        self._other_account_no = None
        self._own_account_no_list = None
        self._page_size = None
        self._sort_type = None
        self._source = None
        self._trans_end_date = None
        self._trans_start_date = None
        self._voucher_id = None

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, value):
        self._current_page = value
    @property
    def dist_memo(self):
        return self._dist_memo

    @dist_memo.setter
    def dist_memo(self, value):
        self._dist_memo = value
    @property
    def dist_type_list(self):
        return self._dist_type_list

    @dist_type_list.setter
    def dist_type_list(self, value):
        if isinstance(value, list):
            self._dist_type_list = list()
            for i in value:
                self._dist_type_list.append(i)
    @property
    def drct_list(self):
        return self._drct_list

    @drct_list.setter
    def drct_list(self, value):
        if isinstance(value, list):
            self._drct_list = list()
            for i in value:
                self._drct_list.append(i)
    @property
    def erecon_biz_type_code(self):
        return self._erecon_biz_type_code

    @erecon_biz_type_code.setter
    def erecon_biz_type_code(self, value):
        self._erecon_biz_type_code = value
    @property
    def fin_biz_code_list(self):
        return self._fin_biz_code_list

    @fin_biz_code_list.setter
    def fin_biz_code_list(self, value):
        if isinstance(value, list):
            self._fin_biz_code_list = list()
            for i in value:
                self._fin_biz_code_list.append(i)
    @property
    def fundlog_source(self):
        return self._fundlog_source

    @fundlog_source.setter
    def fundlog_source(self, value):
        self._fundlog_source = value
    @property
    def inner_account_no(self):
        return self._inner_account_no

    @inner_account_no.setter
    def inner_account_no(self, value):
        self._inner_account_no = value
    @property
    def inst_id_list(self):
        return self._inst_id_list

    @inst_id_list.setter
    def inst_id_list(self, value):
        if isinstance(value, list):
            self._inst_id_list = list()
            for i in value:
                self._inst_id_list.append(i)
    @property
    def inst_serial_no(self):
        return self._inst_serial_no

    @inst_serial_no.setter
    def inst_serial_no(self, value):
        self._inst_serial_no = value
    @property
    def log_status(self):
        return self._log_status

    @log_status.setter
    def log_status(self, value):
        if isinstance(value, list):
            self._log_status = list()
            for i in value:
                self._log_status.append(i)
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def own_account_no_list(self):
        return self._own_account_no_list

    @own_account_no_list.setter
    def own_account_no_list(self, value):
        if isinstance(value, list):
            self._own_account_no_list = list()
            for i in value:
                self._own_account_no_list.append(i)
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def sort_type(self):
        return self._sort_type

    @sort_type.setter
    def sort_type(self, value):
        self._sort_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trans_end_date(self):
        return self._trans_end_date

    @trans_end_date.setter
    def trans_end_date(self, value):
        self._trans_end_date = value
    @property
    def trans_start_date(self):
        return self._trans_start_date

    @trans_start_date.setter
    def trans_start_date(self, value):
        self._trans_start_date = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.current_page:
            if hasattr(self.current_page, 'to_alipay_dict'):
                params['current_page'] = self.current_page.to_alipay_dict()
            else:
                params['current_page'] = self.current_page
        if self.dist_memo:
            if hasattr(self.dist_memo, 'to_alipay_dict'):
                params['dist_memo'] = self.dist_memo.to_alipay_dict()
            else:
                params['dist_memo'] = self.dist_memo
        if self.dist_type_list:
            if isinstance(self.dist_type_list, list):
                for i in range(0, len(self.dist_type_list)):
                    element = self.dist_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dist_type_list[i] = element.to_alipay_dict()
            if hasattr(self.dist_type_list, 'to_alipay_dict'):
                params['dist_type_list'] = self.dist_type_list.to_alipay_dict()
            else:
                params['dist_type_list'] = self.dist_type_list
        if self.drct_list:
            if isinstance(self.drct_list, list):
                for i in range(0, len(self.drct_list)):
                    element = self.drct_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.drct_list[i] = element.to_alipay_dict()
            if hasattr(self.drct_list, 'to_alipay_dict'):
                params['drct_list'] = self.drct_list.to_alipay_dict()
            else:
                params['drct_list'] = self.drct_list
        if self.erecon_biz_type_code:
            if hasattr(self.erecon_biz_type_code, 'to_alipay_dict'):
                params['erecon_biz_type_code'] = self.erecon_biz_type_code.to_alipay_dict()
            else:
                params['erecon_biz_type_code'] = self.erecon_biz_type_code
        if self.fin_biz_code_list:
            if isinstance(self.fin_biz_code_list, list):
                for i in range(0, len(self.fin_biz_code_list)):
                    element = self.fin_biz_code_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fin_biz_code_list[i] = element.to_alipay_dict()
            if hasattr(self.fin_biz_code_list, 'to_alipay_dict'):
                params['fin_biz_code_list'] = self.fin_biz_code_list.to_alipay_dict()
            else:
                params['fin_biz_code_list'] = self.fin_biz_code_list
        if self.fundlog_source:
            if hasattr(self.fundlog_source, 'to_alipay_dict'):
                params['fundlog_source'] = self.fundlog_source.to_alipay_dict()
            else:
                params['fundlog_source'] = self.fundlog_source
        if self.inner_account_no:
            if hasattr(self.inner_account_no, 'to_alipay_dict'):
                params['inner_account_no'] = self.inner_account_no.to_alipay_dict()
            else:
                params['inner_account_no'] = self.inner_account_no
        if self.inst_id_list:
            if isinstance(self.inst_id_list, list):
                for i in range(0, len(self.inst_id_list)):
                    element = self.inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.inst_id_list, 'to_alipay_dict'):
                params['inst_id_list'] = self.inst_id_list.to_alipay_dict()
            else:
                params['inst_id_list'] = self.inst_id_list
        if self.inst_serial_no:
            if hasattr(self.inst_serial_no, 'to_alipay_dict'):
                params['inst_serial_no'] = self.inst_serial_no.to_alipay_dict()
            else:
                params['inst_serial_no'] = self.inst_serial_no
        if self.log_status:
            if isinstance(self.log_status, list):
                for i in range(0, len(self.log_status)):
                    element = self.log_status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.log_status[i] = element.to_alipay_dict()
            if hasattr(self.log_status, 'to_alipay_dict'):
                params['log_status'] = self.log_status.to_alipay_dict()
            else:
                params['log_status'] = self.log_status
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.own_account_no_list:
            if isinstance(self.own_account_no_list, list):
                for i in range(0, len(self.own_account_no_list)):
                    element = self.own_account_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.own_account_no_list[i] = element.to_alipay_dict()
            if hasattr(self.own_account_no_list, 'to_alipay_dict'):
                params['own_account_no_list'] = self.own_account_no_list.to_alipay_dict()
            else:
                params['own_account_no_list'] = self.own_account_no_list
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.sort_type:
            if hasattr(self.sort_type, 'to_alipay_dict'):
                params['sort_type'] = self.sort_type.to_alipay_dict()
            else:
                params['sort_type'] = self.sort_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trans_end_date:
            if hasattr(self.trans_end_date, 'to_alipay_dict'):
                params['trans_end_date'] = self.trans_end_date.to_alipay_dict()
            else:
                params['trans_end_date'] = self.trans_end_date
        if self.trans_start_date:
            if hasattr(self.trans_start_date, 'to_alipay_dict'):
                params['trans_start_date'] = self.trans_start_date.to_alipay_dict()
            else:
                params['trans_start_date'] = self.trans_start_date
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseDocsyncBanklogQueryModel()
        if 'current_page' in d:
            o.current_page = d['current_page']
        if 'dist_memo' in d:
            o.dist_memo = d['dist_memo']
        if 'dist_type_list' in d:
            o.dist_type_list = d['dist_type_list']
        if 'drct_list' in d:
            o.drct_list = d['drct_list']
        if 'erecon_biz_type_code' in d:
            o.erecon_biz_type_code = d['erecon_biz_type_code']
        if 'fin_biz_code_list' in d:
            o.fin_biz_code_list = d['fin_biz_code_list']
        if 'fundlog_source' in d:
            o.fundlog_source = d['fundlog_source']
        if 'inner_account_no' in d:
            o.inner_account_no = d['inner_account_no']
        if 'inst_id_list' in d:
            o.inst_id_list = d['inst_id_list']
        if 'inst_serial_no' in d:
            o.inst_serial_no = d['inst_serial_no']
        if 'log_status' in d:
            o.log_status = d['log_status']
        if 'memo' in d:
            o.memo = d['memo']
        if 'other_account_name' in d:
            o.other_account_name = d['other_account_name']
        if 'other_account_no' in d:
            o.other_account_no = d['other_account_no']
        if 'own_account_no_list' in d:
            o.own_account_no_list = d['own_account_no_list']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'sort_type' in d:
            o.sort_type = d['sort_type']
        if 'source' in d:
            o.source = d['source']
        if 'trans_end_date' in d:
            o.trans_end_date = d['trans_end_date']
        if 'trans_start_date' in d:
            o.trans_start_date = d['trans_start_date']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o



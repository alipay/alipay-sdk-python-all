#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FreightFlowSpdbTradeQueryResultDetail(object):

    def __init__(self):
        self._abstract_content = None
        self._acct_name = None
        self._act_tr_th_dvc_bnk_rpttn = None
        self._act_tr_th_dvry_wy_bnk_nm = None
        self._act_tr_th_dvsry_wy_acct = None
        self._act_tr_th_dvy_wy_ccnt_nm = None
        self._act_tran_date = None
        self._b_dstn_m = None
        self._bids_no = None
        self._channel_seq_no = None
        self._child_acct_nm = None
        self._child_acct_no = None
        self._core_date = None
        self._debit_flag = None
        self._mrch_name = None
        self._mrch_no = None
        self._occur_time = None
        self._post_script = None
        self._remark = None
        self._rsrv_fld = None
        self._settle_acct_no = None
        self._sys_acntg_seq_no = None
        self._sys_tran_seq_no = None
        self._th_dvrsry_acct_bnk_nm = None
        self._th_dvrsry_wc_bnk_rpttn = None
        self._th_dvrsry_wy_acct_no = None
        self._tran_amt = None
        self._tran_cnter_nm = None
        self._tran_date = None
        self._tran_inst_yll = None
        self._tran_seq_srl_no = None
        self._tran_time = None
        self._tran_time_1 = None
        self._tran_tp = None
        self._ylk_tran_seq_no = None
        self._zip_code = None

    @property
    def abstract_content(self):
        return self._abstract_content

    @abstract_content.setter
    def abstract_content(self, value):
        self._abstract_content = value
    @property
    def acct_name(self):
        return self._acct_name

    @acct_name.setter
    def acct_name(self, value):
        self._acct_name = value
    @property
    def act_tr_th_dvc_bnk_rpttn(self):
        return self._act_tr_th_dvc_bnk_rpttn

    @act_tr_th_dvc_bnk_rpttn.setter
    def act_tr_th_dvc_bnk_rpttn(self, value):
        self._act_tr_th_dvc_bnk_rpttn = value
    @property
    def act_tr_th_dvry_wy_bnk_nm(self):
        return self._act_tr_th_dvry_wy_bnk_nm

    @act_tr_th_dvry_wy_bnk_nm.setter
    def act_tr_th_dvry_wy_bnk_nm(self, value):
        self._act_tr_th_dvry_wy_bnk_nm = value
    @property
    def act_tr_th_dvsry_wy_acct(self):
        return self._act_tr_th_dvsry_wy_acct

    @act_tr_th_dvsry_wy_acct.setter
    def act_tr_th_dvsry_wy_acct(self, value):
        self._act_tr_th_dvsry_wy_acct = value
    @property
    def act_tr_th_dvy_wy_ccnt_nm(self):
        return self._act_tr_th_dvy_wy_ccnt_nm

    @act_tr_th_dvy_wy_ccnt_nm.setter
    def act_tr_th_dvy_wy_ccnt_nm(self, value):
        self._act_tr_th_dvy_wy_ccnt_nm = value
    @property
    def act_tran_date(self):
        return self._act_tran_date

    @act_tran_date.setter
    def act_tran_date(self, value):
        self._act_tran_date = value
    @property
    def b_dstn_m(self):
        return self._b_dstn_m

    @b_dstn_m.setter
    def b_dstn_m(self, value):
        self._b_dstn_m = value
    @property
    def bids_no(self):
        return self._bids_no

    @bids_no.setter
    def bids_no(self, value):
        self._bids_no = value
    @property
    def channel_seq_no(self):
        return self._channel_seq_no

    @channel_seq_no.setter
    def channel_seq_no(self, value):
        self._channel_seq_no = value
    @property
    def child_acct_nm(self):
        return self._child_acct_nm

    @child_acct_nm.setter
    def child_acct_nm(self, value):
        self._child_acct_nm = value
    @property
    def child_acct_no(self):
        return self._child_acct_no

    @child_acct_no.setter
    def child_acct_no(self, value):
        self._child_acct_no = value
    @property
    def core_date(self):
        return self._core_date

    @core_date.setter
    def core_date(self, value):
        self._core_date = value
    @property
    def debit_flag(self):
        return self._debit_flag

    @debit_flag.setter
    def debit_flag(self, value):
        self._debit_flag = value
    @property
    def mrch_name(self):
        return self._mrch_name

    @mrch_name.setter
    def mrch_name(self, value):
        self._mrch_name = value
    @property
    def mrch_no(self):
        return self._mrch_no

    @mrch_no.setter
    def mrch_no(self, value):
        self._mrch_no = value
    @property
    def occur_time(self):
        return self._occur_time

    @occur_time.setter
    def occur_time(self, value):
        self._occur_time = value
    @property
    def post_script(self):
        return self._post_script

    @post_script.setter
    def post_script(self, value):
        self._post_script = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def rsrv_fld(self):
        return self._rsrv_fld

    @rsrv_fld.setter
    def rsrv_fld(self, value):
        self._rsrv_fld = value
    @property
    def settle_acct_no(self):
        return self._settle_acct_no

    @settle_acct_no.setter
    def settle_acct_no(self, value):
        self._settle_acct_no = value
    @property
    def sys_acntg_seq_no(self):
        return self._sys_acntg_seq_no

    @sys_acntg_seq_no.setter
    def sys_acntg_seq_no(self, value):
        self._sys_acntg_seq_no = value
    @property
    def sys_tran_seq_no(self):
        return self._sys_tran_seq_no

    @sys_tran_seq_no.setter
    def sys_tran_seq_no(self, value):
        self._sys_tran_seq_no = value
    @property
    def th_dvrsry_acct_bnk_nm(self):
        return self._th_dvrsry_acct_bnk_nm

    @th_dvrsry_acct_bnk_nm.setter
    def th_dvrsry_acct_bnk_nm(self, value):
        self._th_dvrsry_acct_bnk_nm = value
    @property
    def th_dvrsry_wc_bnk_rpttn(self):
        return self._th_dvrsry_wc_bnk_rpttn

    @th_dvrsry_wc_bnk_rpttn.setter
    def th_dvrsry_wc_bnk_rpttn(self, value):
        self._th_dvrsry_wc_bnk_rpttn = value
    @property
    def th_dvrsry_wy_acct_no(self):
        return self._th_dvrsry_wy_acct_no

    @th_dvrsry_wy_acct_no.setter
    def th_dvrsry_wy_acct_no(self, value):
        self._th_dvrsry_wy_acct_no = value
    @property
    def tran_amt(self):
        return self._tran_amt

    @tran_amt.setter
    def tran_amt(self, value):
        self._tran_amt = value
    @property
    def tran_cnter_nm(self):
        return self._tran_cnter_nm

    @tran_cnter_nm.setter
    def tran_cnter_nm(self, value):
        self._tran_cnter_nm = value
    @property
    def tran_date(self):
        return self._tran_date

    @tran_date.setter
    def tran_date(self, value):
        self._tran_date = value
    @property
    def tran_inst_yll(self):
        return self._tran_inst_yll

    @tran_inst_yll.setter
    def tran_inst_yll(self, value):
        self._tran_inst_yll = value
    @property
    def tran_seq_srl_no(self):
        return self._tran_seq_srl_no

    @tran_seq_srl_no.setter
    def tran_seq_srl_no(self, value):
        self._tran_seq_srl_no = value
    @property
    def tran_time(self):
        return self._tran_time

    @tran_time.setter
    def tran_time(self, value):
        self._tran_time = value
    @property
    def tran_time_1(self):
        return self._tran_time_1

    @tran_time_1.setter
    def tran_time_1(self, value):
        self._tran_time_1 = value
    @property
    def tran_tp(self):
        return self._tran_tp

    @tran_tp.setter
    def tran_tp(self, value):
        self._tran_tp = value
    @property
    def ylk_tran_seq_no(self):
        return self._ylk_tran_seq_no

    @ylk_tran_seq_no.setter
    def ylk_tran_seq_no(self, value):
        self._ylk_tran_seq_no = value
    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.abstract_content:
            if hasattr(self.abstract_content, 'to_alipay_dict'):
                params['abstract_content'] = self.abstract_content.to_alipay_dict()
            else:
                params['abstract_content'] = self.abstract_content
        if self.acct_name:
            if hasattr(self.acct_name, 'to_alipay_dict'):
                params['acct_name'] = self.acct_name.to_alipay_dict()
            else:
                params['acct_name'] = self.acct_name
        if self.act_tr_th_dvc_bnk_rpttn:
            if hasattr(self.act_tr_th_dvc_bnk_rpttn, 'to_alipay_dict'):
                params['act_tr_th_dvc_bnk_rpttn'] = self.act_tr_th_dvc_bnk_rpttn.to_alipay_dict()
            else:
                params['act_tr_th_dvc_bnk_rpttn'] = self.act_tr_th_dvc_bnk_rpttn
        if self.act_tr_th_dvry_wy_bnk_nm:
            if hasattr(self.act_tr_th_dvry_wy_bnk_nm, 'to_alipay_dict'):
                params['act_tr_th_dvry_wy_bnk_nm'] = self.act_tr_th_dvry_wy_bnk_nm.to_alipay_dict()
            else:
                params['act_tr_th_dvry_wy_bnk_nm'] = self.act_tr_th_dvry_wy_bnk_nm
        if self.act_tr_th_dvsry_wy_acct:
            if hasattr(self.act_tr_th_dvsry_wy_acct, 'to_alipay_dict'):
                params['act_tr_th_dvsry_wy_acct'] = self.act_tr_th_dvsry_wy_acct.to_alipay_dict()
            else:
                params['act_tr_th_dvsry_wy_acct'] = self.act_tr_th_dvsry_wy_acct
        if self.act_tr_th_dvy_wy_ccnt_nm:
            if hasattr(self.act_tr_th_dvy_wy_ccnt_nm, 'to_alipay_dict'):
                params['act_tr_th_dvy_wy_ccnt_nm'] = self.act_tr_th_dvy_wy_ccnt_nm.to_alipay_dict()
            else:
                params['act_tr_th_dvy_wy_ccnt_nm'] = self.act_tr_th_dvy_wy_ccnt_nm
        if self.act_tran_date:
            if hasattr(self.act_tran_date, 'to_alipay_dict'):
                params['act_tran_date'] = self.act_tran_date.to_alipay_dict()
            else:
                params['act_tran_date'] = self.act_tran_date
        if self.b_dstn_m:
            if hasattr(self.b_dstn_m, 'to_alipay_dict'):
                params['b_dstn_m'] = self.b_dstn_m.to_alipay_dict()
            else:
                params['b_dstn_m'] = self.b_dstn_m
        if self.bids_no:
            if hasattr(self.bids_no, 'to_alipay_dict'):
                params['bids_no'] = self.bids_no.to_alipay_dict()
            else:
                params['bids_no'] = self.bids_no
        if self.channel_seq_no:
            if hasattr(self.channel_seq_no, 'to_alipay_dict'):
                params['channel_seq_no'] = self.channel_seq_no.to_alipay_dict()
            else:
                params['channel_seq_no'] = self.channel_seq_no
        if self.child_acct_nm:
            if hasattr(self.child_acct_nm, 'to_alipay_dict'):
                params['child_acct_nm'] = self.child_acct_nm.to_alipay_dict()
            else:
                params['child_acct_nm'] = self.child_acct_nm
        if self.child_acct_no:
            if hasattr(self.child_acct_no, 'to_alipay_dict'):
                params['child_acct_no'] = self.child_acct_no.to_alipay_dict()
            else:
                params['child_acct_no'] = self.child_acct_no
        if self.core_date:
            if hasattr(self.core_date, 'to_alipay_dict'):
                params['core_date'] = self.core_date.to_alipay_dict()
            else:
                params['core_date'] = self.core_date
        if self.debit_flag:
            if hasattr(self.debit_flag, 'to_alipay_dict'):
                params['debit_flag'] = self.debit_flag.to_alipay_dict()
            else:
                params['debit_flag'] = self.debit_flag
        if self.mrch_name:
            if hasattr(self.mrch_name, 'to_alipay_dict'):
                params['mrch_name'] = self.mrch_name.to_alipay_dict()
            else:
                params['mrch_name'] = self.mrch_name
        if self.mrch_no:
            if hasattr(self.mrch_no, 'to_alipay_dict'):
                params['mrch_no'] = self.mrch_no.to_alipay_dict()
            else:
                params['mrch_no'] = self.mrch_no
        if self.occur_time:
            if hasattr(self.occur_time, 'to_alipay_dict'):
                params['occur_time'] = self.occur_time.to_alipay_dict()
            else:
                params['occur_time'] = self.occur_time
        if self.post_script:
            if hasattr(self.post_script, 'to_alipay_dict'):
                params['post_script'] = self.post_script.to_alipay_dict()
            else:
                params['post_script'] = self.post_script
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.rsrv_fld:
            if hasattr(self.rsrv_fld, 'to_alipay_dict'):
                params['rsrv_fld'] = self.rsrv_fld.to_alipay_dict()
            else:
                params['rsrv_fld'] = self.rsrv_fld
        if self.settle_acct_no:
            if hasattr(self.settle_acct_no, 'to_alipay_dict'):
                params['settle_acct_no'] = self.settle_acct_no.to_alipay_dict()
            else:
                params['settle_acct_no'] = self.settle_acct_no
        if self.sys_acntg_seq_no:
            if hasattr(self.sys_acntg_seq_no, 'to_alipay_dict'):
                params['sys_acntg_seq_no'] = self.sys_acntg_seq_no.to_alipay_dict()
            else:
                params['sys_acntg_seq_no'] = self.sys_acntg_seq_no
        if self.sys_tran_seq_no:
            if hasattr(self.sys_tran_seq_no, 'to_alipay_dict'):
                params['sys_tran_seq_no'] = self.sys_tran_seq_no.to_alipay_dict()
            else:
                params['sys_tran_seq_no'] = self.sys_tran_seq_no
        if self.th_dvrsry_acct_bnk_nm:
            if hasattr(self.th_dvrsry_acct_bnk_nm, 'to_alipay_dict'):
                params['th_dvrsry_acct_bnk_nm'] = self.th_dvrsry_acct_bnk_nm.to_alipay_dict()
            else:
                params['th_dvrsry_acct_bnk_nm'] = self.th_dvrsry_acct_bnk_nm
        if self.th_dvrsry_wc_bnk_rpttn:
            if hasattr(self.th_dvrsry_wc_bnk_rpttn, 'to_alipay_dict'):
                params['th_dvrsry_wc_bnk_rpttn'] = self.th_dvrsry_wc_bnk_rpttn.to_alipay_dict()
            else:
                params['th_dvrsry_wc_bnk_rpttn'] = self.th_dvrsry_wc_bnk_rpttn
        if self.th_dvrsry_wy_acct_no:
            if hasattr(self.th_dvrsry_wy_acct_no, 'to_alipay_dict'):
                params['th_dvrsry_wy_acct_no'] = self.th_dvrsry_wy_acct_no.to_alipay_dict()
            else:
                params['th_dvrsry_wy_acct_no'] = self.th_dvrsry_wy_acct_no
        if self.tran_amt:
            if hasattr(self.tran_amt, 'to_alipay_dict'):
                params['tran_amt'] = self.tran_amt.to_alipay_dict()
            else:
                params['tran_amt'] = self.tran_amt
        if self.tran_cnter_nm:
            if hasattr(self.tran_cnter_nm, 'to_alipay_dict'):
                params['tran_cnter_nm'] = self.tran_cnter_nm.to_alipay_dict()
            else:
                params['tran_cnter_nm'] = self.tran_cnter_nm
        if self.tran_date:
            if hasattr(self.tran_date, 'to_alipay_dict'):
                params['tran_date'] = self.tran_date.to_alipay_dict()
            else:
                params['tran_date'] = self.tran_date
        if self.tran_inst_yll:
            if hasattr(self.tran_inst_yll, 'to_alipay_dict'):
                params['tran_inst_yll'] = self.tran_inst_yll.to_alipay_dict()
            else:
                params['tran_inst_yll'] = self.tran_inst_yll
        if self.tran_seq_srl_no:
            if hasattr(self.tran_seq_srl_no, 'to_alipay_dict'):
                params['tran_seq_srl_no'] = self.tran_seq_srl_no.to_alipay_dict()
            else:
                params['tran_seq_srl_no'] = self.tran_seq_srl_no
        if self.tran_time:
            if hasattr(self.tran_time, 'to_alipay_dict'):
                params['tran_time'] = self.tran_time.to_alipay_dict()
            else:
                params['tran_time'] = self.tran_time
        if self.tran_time_1:
            if hasattr(self.tran_time_1, 'to_alipay_dict'):
                params['tran_time_1'] = self.tran_time_1.to_alipay_dict()
            else:
                params['tran_time_1'] = self.tran_time_1
        if self.tran_tp:
            if hasattr(self.tran_tp, 'to_alipay_dict'):
                params['tran_tp'] = self.tran_tp.to_alipay_dict()
            else:
                params['tran_tp'] = self.tran_tp
        if self.ylk_tran_seq_no:
            if hasattr(self.ylk_tran_seq_no, 'to_alipay_dict'):
                params['ylk_tran_seq_no'] = self.ylk_tran_seq_no.to_alipay_dict()
            else:
                params['ylk_tran_seq_no'] = self.ylk_tran_seq_no
        if self.zip_code:
            if hasattr(self.zip_code, 'to_alipay_dict'):
                params['zip_code'] = self.zip_code.to_alipay_dict()
            else:
                params['zip_code'] = self.zip_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FreightFlowSpdbTradeQueryResultDetail()
        if 'abstract_content' in d:
            o.abstract_content = d['abstract_content']
        if 'acct_name' in d:
            o.acct_name = d['acct_name']
        if 'act_tr_th_dvc_bnk_rpttn' in d:
            o.act_tr_th_dvc_bnk_rpttn = d['act_tr_th_dvc_bnk_rpttn']
        if 'act_tr_th_dvry_wy_bnk_nm' in d:
            o.act_tr_th_dvry_wy_bnk_nm = d['act_tr_th_dvry_wy_bnk_nm']
        if 'act_tr_th_dvsry_wy_acct' in d:
            o.act_tr_th_dvsry_wy_acct = d['act_tr_th_dvsry_wy_acct']
        if 'act_tr_th_dvy_wy_ccnt_nm' in d:
            o.act_tr_th_dvy_wy_ccnt_nm = d['act_tr_th_dvy_wy_ccnt_nm']
        if 'act_tran_date' in d:
            o.act_tran_date = d['act_tran_date']
        if 'b_dstn_m' in d:
            o.b_dstn_m = d['b_dstn_m']
        if 'bids_no' in d:
            o.bids_no = d['bids_no']
        if 'channel_seq_no' in d:
            o.channel_seq_no = d['channel_seq_no']
        if 'child_acct_nm' in d:
            o.child_acct_nm = d['child_acct_nm']
        if 'child_acct_no' in d:
            o.child_acct_no = d['child_acct_no']
        if 'core_date' in d:
            o.core_date = d['core_date']
        if 'debit_flag' in d:
            o.debit_flag = d['debit_flag']
        if 'mrch_name' in d:
            o.mrch_name = d['mrch_name']
        if 'mrch_no' in d:
            o.mrch_no = d['mrch_no']
        if 'occur_time' in d:
            o.occur_time = d['occur_time']
        if 'post_script' in d:
            o.post_script = d['post_script']
        if 'remark' in d:
            o.remark = d['remark']
        if 'rsrv_fld' in d:
            o.rsrv_fld = d['rsrv_fld']
        if 'settle_acct_no' in d:
            o.settle_acct_no = d['settle_acct_no']
        if 'sys_acntg_seq_no' in d:
            o.sys_acntg_seq_no = d['sys_acntg_seq_no']
        if 'sys_tran_seq_no' in d:
            o.sys_tran_seq_no = d['sys_tran_seq_no']
        if 'th_dvrsry_acct_bnk_nm' in d:
            o.th_dvrsry_acct_bnk_nm = d['th_dvrsry_acct_bnk_nm']
        if 'th_dvrsry_wc_bnk_rpttn' in d:
            o.th_dvrsry_wc_bnk_rpttn = d['th_dvrsry_wc_bnk_rpttn']
        if 'th_dvrsry_wy_acct_no' in d:
            o.th_dvrsry_wy_acct_no = d['th_dvrsry_wy_acct_no']
        if 'tran_amt' in d:
            o.tran_amt = d['tran_amt']
        if 'tran_cnter_nm' in d:
            o.tran_cnter_nm = d['tran_cnter_nm']
        if 'tran_date' in d:
            o.tran_date = d['tran_date']
        if 'tran_inst_yll' in d:
            o.tran_inst_yll = d['tran_inst_yll']
        if 'tran_seq_srl_no' in d:
            o.tran_seq_srl_no = d['tran_seq_srl_no']
        if 'tran_time' in d:
            o.tran_time = d['tran_time']
        if 'tran_time_1' in d:
            o.tran_time_1 = d['tran_time_1']
        if 'tran_tp' in d:
            o.tran_tp = d['tran_tp']
        if 'ylk_tran_seq_no' in d:
            o.ylk_tran_seq_no = d['ylk_tran_seq_no']
        if 'zip_code' in d:
            o.zip_code = d['zip_code']
        return o



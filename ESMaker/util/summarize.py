from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.mecab_tokenizer import MeCabTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from pysummarization.nlp_base import NlpBase
from pysummarization.similarityfilter.tfidf_cosine import TfIdfCosine


def summarize(document,similarity_lim):
  # NLPオブジェクト
  nlp_base = NlpBase()
  # トークナイザー設定（MeCab使用）
  nlp_base.tokenizable_doc = MeCabTokenizer()
  # 類似性フィルター
  similarity_filter = TfIdfCosine()
  # NLPオブジェクト設定
  similarity_filter.nlp_base = nlp_base
  # 類似性limit：limit超える文は切り捨て
  similarity_filter.similarity_limit = similarity_lim

  # 自動要約のオブジェクト
  auto_abstractor = AutoAbstractor()
  # トークナイザー設定（MeCab使用）
  auto_abstractor.tokenizable_doc = MeCabTokenizer()
  # 区切り文字設定
  auto_abstractor.delimiter_list = ["。", "\n"]
  # 抽象化&フィルタリングオブジェクト
  abstractable_doc = TopNRankAbstractor()
  # 文書要約（similarity_filter機能追加）
  result_dict = auto_abstractor.summarize(document, abstractable_doc, similarity_filter)

  summarize_result = ""
  # 出力
  for sentence in result_dict["summarize_result"]:
      summarize_result += sentence

  return summarize_result

def best_summarize_doc(document, max_letter):
    limit_list = [lim/100 for lim in range(100)]
    limit_list.reverse()
    for similarity_limit in limit_list:
        summ_doc = summarize(document, similarity_limit)
        if len(summ_doc) <= max_letter:
            return summ_doc

    error_text = str(max_letter) + "文字以下の要約は出来ませんでした。\n"
    return error_text

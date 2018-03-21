from indy_node.server.plugin.agent_authz.constants import ACCUMULATOR_1, \
    ACCUMULATOR_2
from plenum.common.constants import KeyValueStorageType


def get_config(config):
    # NOTE: `AuthzAccumMod` has a dummy value, it will not be used and not of
    # the correct size either
    # config.AuthzAccumMod = 77   # 7*11 = (2*3+1)*(2*5+1)
    config.AuthzAccumMod = {
        ACCUMULATOR_1: 3204629348400311894981147889064213475911502950610822910497794640539580108252311103815602649702091072442089016826192705629222534383850640976103541074965825911439481511841669818218556523699545667979238433531950872370285535430396347665030321087803912182039011247460768098263564546879241877558066260767468387251243972651463237193324761892342299558684399419909028079667195672054655387173203038107042778744649155842364672936664532754000715885900524415403622527226575507346822066350920781137340258848229685505555558665781467456342659911415599377043489979596237979941386501264463874766166877146485965674900595259972161874714381016252770855749700706860768647580178487242906896883599546187195495868346449603306725234279605044720570340541521141682943069084999263530360914420274990375408153529679146137934097158741957518183323298580558730909779698051995609396227449697670716584357361212378371486020465912177797480071144296559699016912326564059836301570632836543118917475972178423287627710340103368809606657431184660768586693677060010145686280797896075497757615632909442703186036300871183851569319692562563918216157762976445282183184528709786306196550055260857987968870798605413506633826598403862811608523439523945519737279157633473140586034211201,
        ACCUMULATOR_2: 3133032080924566959881637452191055160609655524293438819606385720674991596361894869941623022225068918605348030821215520086114403808621280850053350684795125712710087407012772894036421425862560233314314648523623147277999548688559474388879061877185548725118089223823093604853029430403643133732826444283877030142730436440806724215015138813375919445754261729440238895393116059687080047420951044300698828127667739793319375589516868216652624004044627898341937289739315504685938380570351880496638545491909140937856863007811260788811375608394518915419894526073205731567863017762549443787949066965061546426190072082119595112722987549714336192426168846730850256555201637411054474942106140136887446606712629901233511758478704789426507699648599228568443716000256178232838173172583529219810703502190858655879340238882906600390117959887174936452538004363459231760721550955196985907009422925598088870254721647538456683476170050788346184902057773346576532359413370880902716172056325843377330639613774508721179639675066091253808533650050983242491653107140358137874776494507066715820367214766161602433720424953426293579075167196506903155447532819416895145183616697787460722795095532351341246466256478197255754918183172139858779830733597837907514550395373
    }
    # config.AuthzAccumGenerator = 5
    config.AuthzAccumGenerator = {
        ACCUMULATOR_1: 1915182769368569486963976668657418846122016471585262452138689064979880063217142171230525667406114297912997697884669760718181148903891406258652154564474937314809392827351229074850339882653085906709452763512017926382658040877860425398565313118206001571983057266861433787870120516963262872556160137632986790799637800187327525373894833699998137974425675888510468704041321563743266953919273330110447213516904474856325884904918747921700098338253140217925656078220294833113261362981479227102302139442862538529417112227112104830922667359007109709204936925922862592053626140248383988977967399826184116697852122995719423774656923017777301713520425580745782097460248899329835740441429284020663186635354571333690692107185946297929772630086928323118606594588790915139339431940489511850279806818826143040378319619062305629273497273725721368157955512179352674013822087432127910233025333571203452180390613181846035364105352384024395662959142236311712295552933323767329374261596612060957502167831080774021620823718240397211269873903737841346862215246685242302847894894907938934985950908016181737929997451061016202494801606490097096889822976223609532834237496884730642312786447889763148272139117981855545441295507862786712405210727374768044118436617961,
        ACCUMULATOR_2: 3081076980007713925959604505993528370091252037219432570372268594215374344448178557927330505659829548196001541910397044574503804349888018481637021558820201495180652853839389373736354855089915654973646390593825402963369085598243175499331073210996369094524584737045812083227000057867534282991348704391352741963150846904684740081827853667405049291950563131087880761067102663540026285677395840413088174715082923530727315147001628040210198449287076046431564773892455551663145805008468300855353569160670769107273734038564797672775330380086322494841998600095197724618324340015371990124082923120036387971884629120210018406941724331997393028520399574577331410576856213987051688696744981047884734763621690605729499908487228784147873046418572825090779840794201637455940120941399814886616382625317460565896684910105909504707053360780917358988981169951477861282629772514247925341760072523828218731362450851436561547397656679975389798488887044194917116583673849515191323195914776662418177189603969638270971498700371796973381598884749348990545341638774881936625120806067766409748553292974329171798703826943631238764095392265996716384324391039958314190118742197999180964544894121268375540809742303181386694824266665061651735305169041165995833012997227,
    }
    config.AgentAuthzCommitmentDbType = KeyValueStorageType.Leveldb
    config.AgentAuthzCommitmentCacheDbName = 'agent_authz_commitment_cache'
    config.AgentAuthzAccumCommDbType = KeyValueStorageType.Leveldb
    config.AgentAuthzAccum1CommDbName = 'agent_authz_accum1_commitment_db'
    config.AgentAuthzAccum2CommDbName = 'agent_authz_accum2_commitment_db'
    return config
